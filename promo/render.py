"""Export promo/index.html to MP4, GIF and a poster for each caption language.

The page draws every frame as a pure function of time, so this script steps
its clock in 10 ms increments. Every recorded hold time is a multiple of 10 ms,
so each sprite frame lands exactly on time in the 100 fps master.

Usage:
    python promo/render.py --lang ko          # assets/promo-ko.mp4, promo-ko.gif, poster-ko.png
    python promo/render.py --lang en --gif-only
    python promo/render.py --lang ja --stills 0 9000

Needs: playwright (with Chromium), Pillow, numpy, imageio-ffmpeg.
"""
from __future__ import annotations

import argparse
import base64
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
POSTER_TIME_MS = 4600

# The README GIF carries the whole movie at a smaller size; the MP4 linked under it
# is the full-resolution 100 fps master.
GIF_RANGES_MS = [(0, 54200)]
GIF_WIDTH_PX = 640
GIF_HEIGHT_PX = GIF_WIDTH_PX * 9 // 16
GIF_MIN_DELAY_MS = 20       # browsers treat GIF delays under 20 ms as 100 ms
GIF_TARGET_DELAY_MS = 50    # filler frames between sprite changes
GIF_UNCHANGED_INDEX = 255   # transparent palette slot meaning "keep the previous pixel"
GIF_PALETTE_SAMPLES = 48


class QuietRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


# Chromium refuses these ports (net::ERR_UNSAFE_PORT), so a random pick must avoid them.
CHROMIUM_UNSAFE_PORTS = {1719, 1720, 1723, 2049, 3659, 4045, 5060, 5061, 6000, 6566, 6665, 6666, 6667, 6668, 6669, 6697, 10080}


def serve_repo() -> http.server.ThreadingHTTPServer:
    handler = functools.partial(QuietRequestHandler, directory=str(REPO_ROOT))
    while True:
        server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
        if server.server_address[1] not in CHROMIUM_UNSAFE_PORTS:
            break
        server.server_close()
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


class PromoPage:
    def __init__(self, playwright, port: int, query: str):
        self.browser = playwright.chromium.launch()
        self.page = self.browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=1)
        errors = []
        self.page.on("pageerror", lambda error: errors.append(str(error)))
        self.page.goto(f"http://127.0.0.1:{port}/promo/index.html?{query}")
        self.page.evaluate("window.promoReady")
        if errors:
            raise RuntimeError(f"promo page failed: {errors}")
        self.page.add_style_tag(content="canvas{width:1920px!important;height:1080px!important}body{display:block;min-height:0}")
        self.canvas = self.page.locator("#stage")
        self.duration_ms = int(self.page.evaluate("window.PROMO_DURATION_MS"))

    def frame_png(self, time_ms: int) -> bytes:
        # Reading the canvas directly is lighter than a compositor screenshot and
        # survives memory pressure much better on long renders.
        data_url = self.page.evaluate(f"(window.renderAt({time_ms}), document.getElementById('stage').toDataURL('image/png'))")
        return base64.b64decode(data_url.split(",", 1)[1])

    def sprite_signatures(self, start_ms: int, end_ms: int) -> list[str]:
        return self.page.evaluate(
            f"Array.from({{length: {(end_ms - start_ms) // STEP_MS}}}, (_, i) => window.spriteSignatureAt({start_ms} + i * {STEP_MS}))")

    def close(self):
        self.browser.close()


class open_promo:
    """Context manager: a PromoPage served from a throwaway local web server."""

    def __init__(self, query: str):
        self.query = query

    def __enter__(self) -> PromoPage:
        self.server = serve_repo()
        self.playwright = sync_playwright().start()
        self.promo = PromoPage(self.playwright, self.server.server_address[1], self.query)
        return self.promo

    def __exit__(self, *exc):
        self.promo.close()
        self.playwright.stop()
        self.server.shutdown()


def run_ffmpeg(args: list[str], stdin=None):
    command = [imageio_ffmpeg.get_ffmpeg_exe(), "-hide_banner", "-loglevel", "error", "-y", *args]
    return subprocess.Popen(command, stdin=stdin)


BROWSER_RECYCLE_FRAMES = 1000   # a fresh browser every N frames keeps memory flat


def export_mp4(lang: str):
    with open_promo(f"export&lang={lang}") as promo:
        frame_count = promo.duration_ms // STEP_MS
    encoder = run_ffmpeg([
        "-f", "image2pipe", "-framerate", str(1000 // STEP_MS), "-i", "-",
        "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
        "-movflags", "+faststart", str(ASSETS_DIR / f"promo-{lang}.mp4"),
    ], stdin=subprocess.PIPE)
    for chunk_start in range(0, frame_count, BROWSER_RECYCLE_FRAMES):
        with open_promo(f"export&lang={lang}") as promo:
            for index in range(chunk_start, min(frame_count, chunk_start + BROWSER_RECYCLE_FRAMES)):
                time_ms = index * STEP_MS
                png = promo.frame_png(time_ms)
                encoder.stdin.write(png)
                if time_ms == POSTER_TIME_MS:
                    Image.open(io.BytesIO(png)).convert("RGB").save(ASSETS_DIR / f"poster-{lang}.png", optimize=True)
                if index % 500 == 0:
                    print(f"[{lang}] mp4 frame {index}/{frame_count}", flush=True)
    encoder.stdin.close()
    if encoder.wait() != 0:
        raise RuntimeError("MP4 encoding failed")


def choose_gif_times(signatures: list[str], start_ms: int) -> list[int]:
    """Pick frame times that land on every sprite change and keep GIF delays legal."""
    kept: list[tuple[int, bool]] = []  # (time_ms, is_sprite_change)
    for index, signature in enumerate(signatures):
        time_ms = start_ms + index * STEP_MS
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


def export_gif(lang: str):
    """Render the README GIF from clean frames, storing only the pixels that change."""
    with open_promo(f"export&calm&lang={lang}") as promo:
        timeline: list[tuple[int, int]] = []    # (time_ms, display duration)
        for start_ms, end_ms in GIF_RANGES_MS:
            times = choose_gif_times(promo.sprite_signatures(start_ms, end_ms), start_ms)
            segment = [(t, nxt - t) for t, nxt in zip(times, times[1:] + [end_ms])]
            if len(segment) > 1 and segment[-1][1] < GIF_MIN_DELAY_MS:   # fold a too-short tail into its neighbor
                tail = segment.pop()
                segment[-1] = (segment[-1][0], segment[-1][1] + tail[1])
            timeline += segment

        samples = timeline[:: max(1, len(timeline) // GIF_PALETTE_SAMPLES)][:GIF_PALETTE_SAMPLES]
        palette_source = Image.new("RGB", (GIF_WIDTH_PX, GIF_HEIGHT_PX * len(samples)))
        for slot, (time_ms, _) in enumerate(samples):
            palette_source.paste(gif_frame(promo, time_ms), (0, slot * GIF_HEIGHT_PX))
        # 255 real colors; index 255 is a color the art never uses and marks "unchanged"
        palette_image = palette_source.quantize(colors=255, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
        palette_rgb = (palette_image.getpalette()[: 255 * 3] + [0] * 765)[:765] + [255, 0, 255]
        palette_image.putpalette(palette_rgb)

        frames: list[Image.Image] = []      # what each frame should look like
        encoded: list[Image.Image] = []     # what gets written: unchanged pixels become index 255
        previous: np.ndarray | None = None
        for index, (time_ms, _) in enumerate(timeline):
            frame = gif_frame(promo, time_ms).quantize(palette=palette_image, dither=Image.Dither.NONE)
            indices = np.array(frame)
            if (indices == GIF_UNCHANGED_INDEX).any():
                raise RuntimeError("a rendered pixel mapped to the reserved palette index")
            delta = indices.copy()
            if previous is not None:
                delta[indices == previous] = GIF_UNCHANGED_INDEX
            previous = indices
            out = Image.fromarray(delta, mode="P"); out.putpalette(palette_rgb)
            frames.append(frame); encoded.append(out)
            if index % 150 == 0:
                print(f"[{lang}] gif frame {index}/{len(timeline)}", flush=True)

    durations = [duration for _, duration in timeline]
    out_path = ASSETS_DIR / f"promo-{lang}.gif"
    encoded[0].save(out_path, save_all=True, append_images=encoded[1:], duration=durations, loop=0,
                    disposal=1, transparency=GIF_UNCHANGED_INDEX, optimize=False)
    verify_gif(out_path, frames, durations)
    print(f"[{lang}] gif: {len(frames)} frames, {sum(durations)} ms, {out_path.stat().st_size} bytes")


def verify_gif(path: Path, frames: list[Image.Image], durations: list[int]):
    """Decode the written GIF and compare it with the intended frames on a 10 ms timeline."""
    def ticks(images, delays):
        sequence = []
        for image, delay in zip(images, delays):
            sequence += [image] * (delay // STEP_MS)
        return sequence
    decoded, decoded_delays = [], []
    with Image.open(path) as gif:
        for index in range(gif.n_frames):
            gif.seek(index)
            decoded.append(np.array(gif.convert("RGB")))
            decoded_delays.append(gif.info["duration"])
    if min(decoded_delays) < GIF_MIN_DELAY_MS:
        raise RuntimeError(f"GIF has a {min(decoded_delays)} ms frame")
    expected = ticks([np.array(f.convert("RGB")) for f in frames], durations)
    actual = ticks(decoded, decoded_delays)
    if len(expected) != len(actual) or any(not np.array_equal(a, b) for a, b in zip(expected, actual)):
        raise RuntimeError("decoded GIF does not match the rendered frames")


def export_stills(lang: str, times_ms: list[int], out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    with open_promo(f"export&lang={lang}") as promo:
        print(f"duration {promo.duration_ms} ms")
        for time_ms in times_ms:
            (out_dir / f"{lang}_{time_ms:06d}.png").write_bytes(promo.frame_png(time_ms))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--lang", choices=["ko", "en", "ja"], default="ko")
    parser.add_argument("--stills", nargs="*", type=int)
    parser.add_argument("--out", type=Path, default=REPO_ROOT / "promo" / "stills")
    parser.add_argument("--gif-only", action="store_true")
    parser.add_argument("--mp4-only", action="store_true")
    args = parser.parse_args()
    ASSETS_DIR.mkdir(exist_ok=True)
    if args.stills:
        export_stills(args.lang, args.stills, args.out)
    else:
        if not args.gif_only:
            export_mp4(args.lang)
        if not args.mp4_only:
            export_gif(args.lang)
