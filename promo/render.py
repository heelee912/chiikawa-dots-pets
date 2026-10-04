"""Export promo/index.html to MP4, GIF and a README poster.

The page draws every frame as a pure function of time, so this script steps
its clock in 10 ms increments. That keeps every sprite hold exact because all
hold times in the Codex sprite contract are multiples of 10 ms.

Usage:
    python promo/render.py                 # MP4 + GIF + poster into assets/
    python promo/render.py --gif-only      # rebuild only the GIF
    python promo/render.py --stills 0 9000 # PNG stills at the given milliseconds

Needs: playwright (with Chromium), Pillow, numpy, imageio-ffmpeg.
"""
from __future__ import annotations

import argparse
import functools
import http.server
import io
import subprocess
import threading
from pathlib import Path

import imageio_ffmpeg
import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright

REPO_ROOT = Path(__file__).resolve().parent.parent
ASSETS_DIR = REPO_ROOT / "assets"
STEP_MS = 10                # 100 fps master clock
POSTER_TIME_MS = 9600

GIF_WIDTH_PX = 960
GIF_HEIGHT_PX = GIF_WIDTH_PX * 9 // 16
GIF_MIN_DELAY_MS = 20       # browsers treat GIF delays under 20 ms as 100 ms
GIF_TARGET_DELAY_MS = 40    # smooth enough for UI motion between sprite changes
GIF_COLORS = 255            # palette index 255 is reserved for "unchanged" pixels
GIF_UNCHANGED_INDEX = 255
GIF_PALETTE_SAMPLES = 40
# Character and status colors from promo/index.html, kept exact in the GIF palette.
GIF_ACCENT_COLORS = ["#f2a3b3", "#7fb0de", "#efc75e", "#efb24f", "#ad95e0", "#ec8c8c", "#77c99a",
                     "#ffd36e", "#e7a93a", "#5a463d", "#9a8479", "#ead9cc"]


class QuietRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def serve_repo() -> http.server.ThreadingHTTPServer:
    handler = functools.partial(QuietRequestHandler, directory=str(REPO_ROOT))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


class PromoPage:
    def __init__(self, playwright, port: int, query: str = "export"):
        self.browser = playwright.chromium.launch()
        self.page = self.browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=1)
        self.page.goto(f"http://127.0.0.1:{port}/promo/index.html?{query}")
        self.page.evaluate("window.promoReady")
        self.page.add_style_tag(content="canvas{width:1920px!important;height:1080px!important}body{display:block;min-height:0}")
        self.canvas = self.page.locator("#stage")
        self.duration_ms = int(self.page.evaluate("window.PROMO_DURATION_MS"))

    def frame_png(self, time_ms: int) -> bytes:
        self.page.evaluate(f"window.renderAt({time_ms})")
        return self.canvas.screenshot(type="png")

    def sprite_signatures(self) -> list[str]:
        frame_count = self.duration_ms // STEP_MS
        return self.page.evaluate(f"Array.from({{length: {frame_count}}}, (_, i) => window.spriteSignatureAt(i * {STEP_MS}))")

    def close(self):
        self.browser.close()


def open_promo(query: str = "export"):
    """Context helper: yields a PromoPage served from a throwaway local web server."""
    class _Session:
        def __enter__(self):
            self.server = serve_repo()
            self.playwright = sync_playwright().start()
            self.promo = PromoPage(self.playwright, self.server.server_address[1], query)
            return self.promo

        def __exit__(self, *exc):
            self.promo.close()
            self.playwright.stop()
            self.server.shutdown()

    return _Session()


def run_ffmpeg(args: list[str], stdin=None):
    command = [imageio_ffmpeg.get_ffmpeg_exe(), "-hide_banner", "-loglevel", "error", "-y", *args]
    return subprocess.Popen(command, stdin=stdin)


def export_mp4():
    with open_promo() as promo:
        frame_count = promo.duration_ms // STEP_MS
        encoder = run_ffmpeg([
            "-f", "image2pipe", "-framerate", str(1000 // STEP_MS), "-i", "-",
            "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p",
            "-movflags", "+faststart", str(ASSETS_DIR / "promo.mp4"),
        ], stdin=subprocess.PIPE)
        for index in range(frame_count):
            time_ms = index * STEP_MS
            png = promo.frame_png(time_ms)
            encoder.stdin.write(png)
            if time_ms == POSTER_TIME_MS:
                Image.open(io.BytesIO(png)).convert("RGB").save(ASSETS_DIR / "poster.png", optimize=True)
            if index % 250 == 0:
                print(f"mp4 frame {index}/{frame_count}", flush=True)
        encoder.stdin.close()
        if encoder.wait() != 0:
            raise RuntimeError("MP4 encoding failed")


def choose_gif_times(signatures: list[str]) -> list[int]:
    """Pick frame times that land exactly on every sprite change and keep GIF delays legal."""
    kept: list[tuple[int, bool]] = []  # (time_ms, is_sprite_change)
    for index, signature in enumerate(signatures):
        time_ms = index * STEP_MS
        is_change = index == 0 or signature != signatures[index - 1]
        gap_ms = time_ms - kept[-1][0] if kept else GIF_TARGET_DELAY_MS
        if is_change and gap_ms >= GIF_MIN_DELAY_MS:
            kept.append((time_ms, True))
        elif is_change and not kept[-1][1]:
            kept[-1] = (time_ms, True)          # replace a filler frame instead of crowding it
        elif gap_ms >= GIF_TARGET_DELAY_MS:
            kept.append((time_ms, False))
    return [time_ms for time_ms, _ in kept]


def gif_frame(promo: PromoPage, time_ms: int) -> Image.Image:
    png = promo.frame_png(time_ms)
    return Image.open(io.BytesIO(png)).convert("RGB").resize((GIF_WIDTH_PX, GIF_HEIGHT_PX), Image.LANCZOS)


def export_gif():
    """Render the README GIF from clean frames, storing only the pixels that change."""
    with open_promo("export&calm") as promo:
        signatures = promo.sprite_signatures()
        times_ms = choose_gif_times(signatures)
        total_ms = len(signatures) * STEP_MS

        # One shared palette keeps colors steady; no dithering keeps flat areas compressible.
        # A swatch strip guarantees the small accent colors survive median-cut quantization.
        sample_times = times_ms[:: max(1, len(times_ms) // GIF_PALETTE_SAMPLES)][:GIF_PALETTE_SAMPLES]
        palette_source = Image.new("RGB", (GIF_WIDTH_PX, GIF_HEIGHT_PX * (len(sample_times) + 1)))
        for slot, time_ms in enumerate(sample_times):
            palette_source.paste(gif_frame(promo, time_ms), (0, slot * GIF_HEIGHT_PX))
        swatch_width_px = GIF_WIDTH_PX // len(GIF_ACCENT_COLORS)
        for slot, color in enumerate(GIF_ACCENT_COLORS):
            palette_source.paste(color, (slot * swatch_width_px, len(sample_times) * GIF_HEIGHT_PX,
                                         (slot + 1) * swatch_width_px, (len(sample_times) + 1) * GIF_HEIGHT_PX))
        palette_image = palette_source.quantize(colors=GIF_COLORS, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
        palette_rgb = palette_image.getpalette()[: GIF_COLORS * 3]
        palette_rgb += [255, 0, 255] * (256 - GIF_COLORS)  # index 255: never displayed, marks transparency

        frames: list[Image.Image] = []
        previous: np.ndarray | None = None
        for index, time_ms in enumerate(times_ms):
            indices = np.array(gif_frame(promo, time_ms).quantize(palette=palette_image, dither=Image.Dither.NONE))
            encoded = indices.copy()
            if previous is not None:
                encoded[indices == previous] = GIF_UNCHANGED_INDEX
            previous = indices
            frame = Image.fromarray(encoded, mode="P")
            frame.putpalette(palette_rgb)
            frames.append(frame)
            if index % 100 == 0:
                print(f"gif frame {index}/{len(times_ms)}", flush=True)

    durations_ms = [following - current for current, following in zip(times_ms, times_ms[1:] + [total_ms])]
    frames[0].save(ASSETS_DIR / "promo.gif", save_all=True, append_images=frames[1:], duration=durations_ms,
                   loop=0, disposal=1, transparency=GIF_UNCHANGED_INDEX, optimize=False)
    print(f"gif: {len(frames)} frames, {sum(durations_ms)} ms")


def export_stills(times_ms: list[int], out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    with open_promo() as promo:
        print(f"duration {promo.duration_ms} ms")
        for time_ms in times_ms:
            (out_dir / f"still_{time_ms:06d}.png").write_bytes(promo.frame_png(time_ms))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--stills", nargs="*", type=int)
    parser.add_argument("--out", type=Path, default=REPO_ROOT / "promo" / "stills")
    parser.add_argument("--gif-only", action="store_true", help="rebuild only promo.gif")
    args = parser.parse_args()
    ASSETS_DIR.mkdir(exist_ok=True)
    if args.stills:
        export_stills(args.stills, args.out)
    elif args.gif_only:
        export_gif()
    else:
        export_mp4()
        export_gif()
