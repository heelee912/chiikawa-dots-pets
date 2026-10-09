<div align="center">

# Chiikawa Dots Pets

**Eleven Chiikawa friends as Codex desktop pets**

[한국어](README.md) · [English](README.en.md) · [日本語](README.ja.md)

<img src="assets/promo-en.gif" alt="Eleven Chiikawa friends react to the work beside a window and run to the middle of the screen where they follow the cursor and jump together" width="100%">

[Watch in full quality (MP4 · 1080p · 100fps)](assets/promo-en.mp4) · [Download releases](https://github.com/heelee912/chiikawa-dots-pets/releases/latest)

</div>

---

Bring **eleven** Chiikawa friends to the Codex desktop app as animated pets.
Every pet follows the **Codex pet v2 format** (an 8 × 11 grid of 192 × 208 cells on a 1536 × 2288 transparent PNG) with nine state animations and a 16-direction look loop.

## Characters

<table>
<tr><td align="center"><img src="assets/motions/chiikawa/idle.gif" width="96" alt="Chiikawa"><br><sub>Chiikawa<br><code>chiikawa</code></sub></td><td align="center"><img src="assets/motions/hachiware/idle.gif" width="96" alt="Hachiware"><br><sub>Hachiware<br><code>hachiware</code></sub></td><td align="center"><img src="assets/motions/usagi/idle.gif" width="96" alt="Usagi"><br><sub>Usagi<br><code>usagi</code></sub></td><td align="center"><img src="assets/motions/momonga/idle.gif" width="96" alt="Momonga"><br><sub>Momonga<br><code>momonga</code></sub></td><td align="center"><img src="assets/motions/shisa/idle.gif" width="96" alt="Shisa"><br><sub>Shisa<br><code>shisa</code></sub></td><td align="center"><img src="assets/motions/rakko/idle.gif" width="96" alt="Rakko"><br><sub>Rakko<br><code>rakko</code></sub></td></tr>
<tr><td align="center"><img src="assets/motions/kurimanju/idle.gif" width="96" alt="Kurimanju"><br><sub>Kurimanju<br><code>kurimanju</code></sub></td><td align="center"><img src="assets/motions/siren/idle.gif" width="96" alt="Siren"><br><sub>Siren<br><code>siren</code></sub></td><td align="center"><img src="assets/motions/furuhonya/idle.gif" width="96" alt="Furuhonya"><br><sub>Furuhonya<br><code>furuhonya</code></sub></td><td align="center"><img src="assets/motions/anoko/idle.gif" width="96" alt="Anoko"><br><sub>Anoko<br><code>anoko</code></sub></td><td align="center"><img src="assets/motions/dekatsuyo/idle.gif" width="96" alt="Dekatsuyo"><br><sub>Dekatsuyo<br><code>dekatsuyo</code></sub></td></tr>
</table>

## Install

### One-line install

**Windows (PowerShell)**

```powershell
irm https://raw.githubusercontent.com/heelee912/chiikawa-dots-pets/main/install.ps1 | iex
```

**macOS · Linux**

```bash
curl -fsSL https://raw.githubusercontent.com/heelee912/chiikawa-dots-pets/main/install.sh | sh
```

This installs all eleven pets. Set `CHIIKAWA_PETS` to a list of pet IDs to install only some. Restart Codex and pick a pet from its pet list.

```powershell
$env:CHIIKAWA_PETS = "chiikawa,momonga"; irm https://raw.githubusercontent.com/heelee912/chiikawa-dots-pets/main/install.ps1 | iex
```

### Manual install

Download a zip from the [latest release](https://github.com/heelee912/chiikawa-dots-pets/releases/latest) and put each pet folder (`pet.json` + `spritesheet.png`) under `~/.codex/pets/`. On Windows that is `%USERPROFILE%\.codex\pets\`.

## Motion gallery

Every motion is the approved original and keeps its recorded frame timing.

<table>
<tr><th></th><th><sub>Idle</sub></th><th><sub>Run →</sub></th><th><sub>Run ←</sub></th><th><sub>Wave</sub></th><th><sub>Jump</sub></th><th><sub>Failed</sub></th><th><sub>Waiting</sub></th><th><sub>Working</sub></th><th><sub>Review</sub></th><th><sub>16-way look</sub></th></tr>
<tr><th><sub>Chiikawa</sub></th><td><img src="assets/motions/chiikawa/idle.gif" width="72" alt="Chiikawa Idle"></td><td><img src="assets/motions/chiikawa/running-right.gif" width="72" alt="Chiikawa Run →"></td><td><img src="assets/motions/chiikawa/running-left.gif" width="72" alt="Chiikawa Run ←"></td><td><img src="assets/motions/chiikawa/waving.gif" width="72" alt="Chiikawa Wave"></td><td><img src="assets/motions/chiikawa/jumping.gif" width="72" alt="Chiikawa Jump"></td><td><img src="assets/motions/chiikawa/failed.gif" width="72" alt="Chiikawa Failed"></td><td><img src="assets/motions/chiikawa/waiting.gif" width="72" alt="Chiikawa Waiting"></td><td><img src="assets/motions/chiikawa/running.gif" width="72" alt="Chiikawa Working"></td><td><img src="assets/motions/chiikawa/review.gif" width="72" alt="Chiikawa Review"></td><td><img src="assets/motions/chiikawa/look.gif" width="72" alt="Chiikawa 16-way look"></td></tr>
<tr><th><sub>Hachiware</sub></th><td><img src="assets/motions/hachiware/idle.gif" width="72" alt="Hachiware Idle"></td><td><img src="assets/motions/hachiware/running-right.gif" width="72" alt="Hachiware Run →"></td><td><img src="assets/motions/hachiware/running-left.gif" width="72" alt="Hachiware Run ←"></td><td><img src="assets/motions/hachiware/waving.gif" width="72" alt="Hachiware Wave"></td><td><img src="assets/motions/hachiware/jumping.gif" width="72" alt="Hachiware Jump"></td><td><img src="assets/motions/hachiware/failed.gif" width="72" alt="Hachiware Failed"></td><td><img src="assets/motions/hachiware/waiting.gif" width="72" alt="Hachiware Waiting"></td><td><img src="assets/motions/hachiware/running.gif" width="72" alt="Hachiware Working"></td><td><img src="assets/motions/hachiware/review.gif" width="72" alt="Hachiware Review"></td><td><img src="assets/motions/hachiware/look.gif" width="72" alt="Hachiware 16-way look"></td></tr>
<tr><th><sub>Usagi</sub></th><td><img src="assets/motions/usagi/idle.gif" width="72" alt="Usagi Idle"></td><td><img src="assets/motions/usagi/running-right.gif" width="72" alt="Usagi Run →"></td><td><img src="assets/motions/usagi/running-left.gif" width="72" alt="Usagi Run ←"></td><td><img src="assets/motions/usagi/waving.gif" width="72" alt="Usagi Wave"></td><td><img src="assets/motions/usagi/jumping.gif" width="72" alt="Usagi Jump"></td><td><img src="assets/motions/usagi/failed.gif" width="72" alt="Usagi Failed"></td><td><img src="assets/motions/usagi/waiting.gif" width="72" alt="Usagi Waiting"></td><td><img src="assets/motions/usagi/running.gif" width="72" alt="Usagi Working"></td><td><img src="assets/motions/usagi/review.gif" width="72" alt="Usagi Review"></td><td><img src="assets/motions/usagi/look.gif" width="72" alt="Usagi 16-way look"></td></tr>
<tr><th><sub>Momonga</sub></th><td><img src="assets/motions/momonga/idle.gif" width="72" alt="Momonga Idle"></td><td><img src="assets/motions/momonga/running-right.gif" width="72" alt="Momonga Run →"></td><td><img src="assets/motions/momonga/running-left.gif" width="72" alt="Momonga Run ←"></td><td><img src="assets/motions/momonga/waving.gif" width="72" alt="Momonga Wave"></td><td><img src="assets/motions/momonga/jumping.gif" width="72" alt="Momonga Jump"></td><td><img src="assets/motions/momonga/failed.gif" width="72" alt="Momonga Failed"></td><td><img src="assets/motions/momonga/waiting.gif" width="72" alt="Momonga Waiting"></td><td><img src="assets/motions/momonga/running.gif" width="72" alt="Momonga Working"></td><td><img src="assets/motions/momonga/review.gif" width="72" alt="Momonga Review"></td><td><img src="assets/motions/momonga/look.gif" width="72" alt="Momonga 16-way look"></td></tr>
<tr><th><sub>Shisa</sub></th><td><img src="assets/motions/shisa/idle.gif" width="72" alt="Shisa Idle"></td><td><img src="assets/motions/shisa/running-right.gif" width="72" alt="Shisa Run →"></td><td><img src="assets/motions/shisa/running-left.gif" width="72" alt="Shisa Run ←"></td><td><img src="assets/motions/shisa/waving.gif" width="72" alt="Shisa Wave"></td><td><img src="assets/motions/shisa/jumping.gif" width="72" alt="Shisa Jump"></td><td><img src="assets/motions/shisa/failed.gif" width="72" alt="Shisa Failed"></td><td><img src="assets/motions/shisa/waiting.gif" width="72" alt="Shisa Waiting"></td><td><img src="assets/motions/shisa/running.gif" width="72" alt="Shisa Working"></td><td><img src="assets/motions/shisa/review.gif" width="72" alt="Shisa Review"></td><td><img src="assets/motions/shisa/look.gif" width="72" alt="Shisa 16-way look"></td></tr>
<tr><th><sub>Rakko</sub></th><td><img src="assets/motions/rakko/idle.gif" width="72" alt="Rakko Idle"></td><td><img src="assets/motions/rakko/running-right.gif" width="72" alt="Rakko Run →"></td><td><img src="assets/motions/rakko/running-left.gif" width="72" alt="Rakko Run ←"></td><td><img src="assets/motions/rakko/waving.gif" width="72" alt="Rakko Wave"></td><td><img src="assets/motions/rakko/jumping.gif" width="72" alt="Rakko Jump"></td><td><img src="assets/motions/rakko/failed.gif" width="72" alt="Rakko Failed"></td><td><img src="assets/motions/rakko/waiting.gif" width="72" alt="Rakko Waiting"></td><td><img src="assets/motions/rakko/running.gif" width="72" alt="Rakko Working"></td><td><img src="assets/motions/rakko/review.gif" width="72" alt="Rakko Review"></td><td><img src="assets/motions/rakko/look.gif" width="72" alt="Rakko 16-way look"></td></tr>
<tr><th><sub>Kurimanju</sub></th><td><img src="assets/motions/kurimanju/idle.gif" width="72" alt="Kurimanju Idle"></td><td><img src="assets/motions/kurimanju/running-right.gif" width="72" alt="Kurimanju Run →"></td><td><img src="assets/motions/kurimanju/running-left.gif" width="72" alt="Kurimanju Run ←"></td><td><img src="assets/motions/kurimanju/waving.gif" width="72" alt="Kurimanju Wave"></td><td><img src="assets/motions/kurimanju/jumping.gif" width="72" alt="Kurimanju Jump"></td><td><img src="assets/motions/kurimanju/failed.gif" width="72" alt="Kurimanju Failed"></td><td><img src="assets/motions/kurimanju/waiting.gif" width="72" alt="Kurimanju Waiting"></td><td><img src="assets/motions/kurimanju/running.gif" width="72" alt="Kurimanju Working"></td><td><img src="assets/motions/kurimanju/review.gif" width="72" alt="Kurimanju Review"></td><td><img src="assets/motions/kurimanju/look.gif" width="72" alt="Kurimanju 16-way look"></td></tr>
<tr><th><sub>Siren</sub></th><td><img src="assets/motions/siren/idle.gif" width="72" alt="Siren Idle"></td><td><img src="assets/motions/siren/running-right.gif" width="72" alt="Siren Run →"></td><td><img src="assets/motions/siren/running-left.gif" width="72" alt="Siren Run ←"></td><td><img src="assets/motions/siren/waving.gif" width="72" alt="Siren Wave"></td><td><img src="assets/motions/siren/jumping.gif" width="72" alt="Siren Jump"></td><td><img src="assets/motions/siren/failed.gif" width="72" alt="Siren Failed"></td><td><img src="assets/motions/siren/waiting.gif" width="72" alt="Siren Waiting"></td><td><img src="assets/motions/siren/running.gif" width="72" alt="Siren Working"></td><td><img src="assets/motions/siren/review.gif" width="72" alt="Siren Review"></td><td><img src="assets/motions/siren/look.gif" width="72" alt="Siren 16-way look"></td></tr>
<tr><th><sub>Furuhonya</sub></th><td><img src="assets/motions/furuhonya/idle.gif" width="72" alt="Furuhonya Idle"></td><td><img src="assets/motions/furuhonya/running-right.gif" width="72" alt="Furuhonya Run →"></td><td><img src="assets/motions/furuhonya/running-left.gif" width="72" alt="Furuhonya Run ←"></td><td><img src="assets/motions/furuhonya/waving.gif" width="72" alt="Furuhonya Wave"></td><td><img src="assets/motions/furuhonya/jumping.gif" width="72" alt="Furuhonya Jump"></td><td><img src="assets/motions/furuhonya/failed.gif" width="72" alt="Furuhonya Failed"></td><td><img src="assets/motions/furuhonya/waiting.gif" width="72" alt="Furuhonya Waiting"></td><td><img src="assets/motions/furuhonya/running.gif" width="72" alt="Furuhonya Working"></td><td><img src="assets/motions/furuhonya/review.gif" width="72" alt="Furuhonya Review"></td><td><img src="assets/motions/furuhonya/look.gif" width="72" alt="Furuhonya 16-way look"></td></tr>
<tr><th><sub>Anoko</sub></th><td><img src="assets/motions/anoko/idle.gif" width="72" alt="Anoko Idle"></td><td><img src="assets/motions/anoko/running-right.gif" width="72" alt="Anoko Run →"></td><td><img src="assets/motions/anoko/running-left.gif" width="72" alt="Anoko Run ←"></td><td><img src="assets/motions/anoko/waving.gif" width="72" alt="Anoko Wave"></td><td><img src="assets/motions/anoko/jumping.gif" width="72" alt="Anoko Jump"></td><td><img src="assets/motions/anoko/failed.gif" width="72" alt="Anoko Failed"></td><td><img src="assets/motions/anoko/waiting.gif" width="72" alt="Anoko Waiting"></td><td><img src="assets/motions/anoko/running.gif" width="72" alt="Anoko Working"></td><td><img src="assets/motions/anoko/review.gif" width="72" alt="Anoko Review"></td><td><img src="assets/motions/anoko/look.gif" width="72" alt="Anoko 16-way look"></td></tr>
<tr><th><sub>Dekatsuyo</sub></th><td><img src="assets/motions/dekatsuyo/idle.gif" width="72" alt="Dekatsuyo Idle"></td><td><img src="assets/motions/dekatsuyo/running-right.gif" width="72" alt="Dekatsuyo Run →"></td><td><img src="assets/motions/dekatsuyo/running-left.gif" width="72" alt="Dekatsuyo Run ←"></td><td><img src="assets/motions/dekatsuyo/waving.gif" width="72" alt="Dekatsuyo Wave"></td><td><img src="assets/motions/dekatsuyo/jumping.gif" width="72" alt="Dekatsuyo Jump"></td><td><img src="assets/motions/dekatsuyo/failed.gif" width="72" alt="Dekatsuyo Failed"></td><td><img src="assets/motions/dekatsuyo/waiting.gif" width="72" alt="Dekatsuyo Waiting"></td><td><img src="assets/motions/dekatsuyo/running.gif" width="72" alt="Dekatsuyo Working"></td><td><img src="assets/motions/dekatsuyo/review.gif" width="72" alt="Dekatsuyo Review"></td><td><img src="assets/motions/dekatsuyo/look.gif" width="72" alt="Dekatsuyo 16-way look"></td></tr>
</table>

> The Codex state `running` means busy working, so it is the **Working** motion here. Running across the screen is `running-right` and `running-left`.

<details>
<summary>Sprite format</summary>

| Row | State | Frames |
|:-:|:--|:-:|
| 0 | idle | 6 |
| 1 | running-right | 8 |
| 2 | running-left | 8 |
| 3 | waving | 4 |
| 4 | jumping | 5 |
| 5 | failed | 8 |
| 6 | waiting | 6 |
| 7 | running | 6 |
| 8 | review | 6 |
| 9 – 10 | look, 16 directions clockwise from 12 o'clock | 16 |

```json
{
  "id": "chiikawa",
  "displayName": "Chiikawa",
  "description": "Chiikawa from Chiikawa as a Codex desktop pet.",
  "spriteVersionNumber": 2,
  "spritesheetPath": "spritesheet.png"
}
```

</details>

## Notice

This is an unofficial fan project. Chiikawa and all related characters belong to Nagano and their respective rights holders. The sprites carry no license for commercial use or redistribution, and they will be taken down on request.
