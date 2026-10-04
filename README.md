<div align="center">

# Chiikawa Dots Pets

**치이카와 · 하치와레 · 우사기, 3인방을 Codex 데스크톱 펫으로**

<img src="assets/promo.gif" alt="치이카와 3인방이 등장해 달리고 인사한 뒤 Codex 상태별 모션과 16방향 시선을 보여 주는 소개 영상" width="100%">

[고화질 MP4로 보기 (1080p · 100fps)](assets/promo.mp4) · [릴리즈 다운로드](https://github.com/heelee912/chiikawa-dots-pets/releases/latest) · [설치하기](#설치) · [모션 둘러보기](#모션-둘러보기) · [English](#english)

</div>

---

## 소개

Codex 데스크톱 앱의 펫 기능에서 쓸 수 있는 치이카와 3인방 스프라이트입니다.
세 캐릭터 모두 **Codex 펫 v2 규격**(8열 × 11행 · 셀 192 × 208 · 1536 × 2288 투명 PNG)을 따르고 9가지 상태 모션과 16방향 시선을 모두 갖추고 있습니다.

| | 치이카와 | 하치와레 | 우사기 |
|:-:|:-:|:-:|:-:|
| 전체 모션 | <img src="assets/motions/chiikawa/all_motions.gif" width="144" alt="치이카와 전체 모션"> | <img src="assets/motions/hachiware/all_motions.gif" width="144" alt="하치와레 전체 모션"> | <img src="assets/motions/usagi/all_motions.gif" width="144" alt="우사기 전체 모션"> |
| 펫 ID | `chiikawa` | `hachiware` | `usagi` |
| 스프라이트 | [spritesheet.png](pets/chiikawa/spritesheet.png) | [spritesheet.png](pets/hachiware/spritesheet.png) | [spritesheet.png](pets/usagi/spritesheet.png) |

## 설치

Codex는 `~/.codex/pets/<펫 ID>/` 폴더에 있는 `pet.json`과 `spritesheet.png`를 읽어 커스텀 펫으로 불러옵니다.
설치가 끝나면 Codex를 다시 시작하고 펫 목록에서 원하는 캐릭터를 고르세요.

### 한 줄 설치

**Windows (PowerShell)**

```powershell
irm https://raw.githubusercontent.com/heelee912/chiikawa-dots-pets/main/install.ps1 | iex
```

**macOS · Linux**

```bash
curl -fsSL https://raw.githubusercontent.com/heelee912/chiikawa-dots-pets/main/install.sh | sh
```

세 캐릭터가 모두 설치됩니다. 일부만 원하면 `CHIIKAWA_PETS` 환경 변수로 고를 수 있습니다.

```powershell
$env:CHIIKAWA_PETS = "chiikawa,usagi"; irm https://raw.githubusercontent.com/heelee912/chiikawa-dots-pets/main/install.ps1 | iex
```

```bash
curl -fsSL https://raw.githubusercontent.com/heelee912/chiikawa-dots-pets/main/install.sh | CHIIKAWA_PETS="chiikawa usagi" sh
```

`CODEX_HOME`을 따로 지정해 두었다면 그 경로 아래 `pets` 폴더에 설치됩니다.

### 직접 설치

1. [최신 릴리즈](https://github.com/heelee912/chiikawa-dots-pets/releases/latest)에서 `chiikawa-dots-pets-all.zip`이나 캐릭터별 zip을 내려받습니다.
2. 캐릭터 폴더를 통째로 Codex 펫 폴더에 넣습니다. (캐릭터별 zip은 `pets/<펫 ID>/` 폴더를 만든 뒤 그 안에 풉니다.)
   - Windows: `%USERPROFILE%\.codex\pets\`
   - macOS · Linux: `~/.codex/pets/`
3. 결과가 아래처럼 되면 됩니다.

```text
.codex/pets/
├── chiikawa/
│   ├── pet.json
│   └── spritesheet.png
├── hachiware/
└── usagi/
```

스프라이트 원본을 직접 등록하는 방식을 쓴다면 각 폴더의 `spritesheet.png`를 그대로 사용하면 됩니다. 파일은 가공 없이 최종본 그대로 올려 두었습니다.

## 모션 둘러보기

모든 프레임은 원래 지정된 재생 간격 그대로입니다.

| 모션 | Codex 상태 | 치이카와 | 하치와레 | 우사기 |
|:--|:--|:-:|:-:|:-:|
| 쉬기 | `idle` | <img src="assets/motions/chiikawa/idle.gif" width="96"> | <img src="assets/motions/hachiware/idle.gif" width="96"> | <img src="assets/motions/usagi/idle.gif" width="96"> |
| 오른쪽 달리기 | `running-right` | <img src="assets/motions/chiikawa/running-right.gif" width="96"> | <img src="assets/motions/hachiware/running-right.gif" width="96"> | <img src="assets/motions/usagi/running-right.gif" width="96"> |
| 왼쪽 달리기 | `running-left` | <img src="assets/motions/chiikawa/running-left.gif" width="96"> | <img src="assets/motions/hachiware/running-left.gif" width="96"> | <img src="assets/motions/usagi/running-left.gif" width="96"> |
| 인사 | `waving` | <img src="assets/motions/chiikawa/waving.gif" width="96"> | <img src="assets/motions/hachiware/waving.gif" width="96"> | <img src="assets/motions/usagi/waving.gif" width="96"> |
| 점프 | `jumping` | <img src="assets/motions/chiikawa/jumping.gif" width="96"> | <img src="assets/motions/hachiware/jumping.gif" width="96"> | <img src="assets/motions/usagi/jumping.gif" width="96"> |
| 실패 반응 | `failed` | <img src="assets/motions/chiikawa/failed.gif" width="96"> | <img src="assets/motions/hachiware/failed.gif" width="96"> | <img src="assets/motions/usagi/failed.gif" width="96"> |
| 기다림 | `waiting` | <img src="assets/motions/chiikawa/waiting.gif" width="96"> | <img src="assets/motions/hachiware/waiting.gif" width="96"> | <img src="assets/motions/usagi/waiting.gif" width="96"> |
| 생각 | `running` | <img src="assets/motions/chiikawa/running.gif" width="96"> | <img src="assets/motions/hachiware/running.gif" width="96"> | <img src="assets/motions/usagi/running.gif" width="96"> |
| 검토 | `review` | <img src="assets/motions/chiikawa/review.gif" width="96"> | <img src="assets/motions/hachiware/review.gif" width="96"> | <img src="assets/motions/usagi/review.gif" width="96"> |
| 시선 16방향 | `look` | <img src="assets/motions/chiikawa/look.gif" width="96"> | <img src="assets/motions/hachiware/look.gif" width="96"> | <img src="assets/motions/usagi/look.gif" width="96"> |

> Codex 내부 상태 이름 `running`은 작업 중이라는 뜻이라 여기서는 **생각** 모션입니다. 화면 위를 달리는 모션은 `running-right`와 `running-left`입니다.
> 시선 미리보기는 위쪽(12시)에서 시작해 시계 방향으로 22.5도씩 돌며 확인하기 쉽게 한 방향당 180ms로 재생합니다.

<details>
<summary>스프라이트 규격 자세히 보기</summary>

| 행 | 상태 | 프레임 | 재생 간격 (ms) |
|:-:|:--|:-:|:--|
| 0 | idle | 6 | 280 · 110 · 110 · 140 · 140 · 320 |
| 1 | running-right | 8 | 120 × 7 · 220 |
| 2 | running-left | 8 | 120 × 7 · 220 |
| 3 | waving | 4 | 140 × 3 · 280 |
| 4 | jumping | 5 | 140 × 4 · 280 |
| 5 | failed | 8 | 140 × 7 · 240 |
| 6 | waiting | 6 | 150 × 5 · 260 |
| 7 | running | 6 | 120 × 5 · 220 |
| 8 | review | 6 | 150 × 5 · 280 |
| 9 | look 0° ~ 157.5° | 8 | 위쪽부터 시계 방향 |
| 10 | look 180° ~ 337.5° | 8 | 아래쪽부터 시계 방향 |

`pet.json` 예시:

```json
{
  "id": "chiikawa",
  "displayName": "Chiikawa",
  "description": "A small and kind of cute little friend who tries their best.",
  "spriteVersionNumber": 2,
  "spritesheetPath": "spritesheet.png"
}
```

</details>

## 소개 영상 다시 만들기

맨 위 영상은 [`promo/index.html`](promo/index.html)이 캔버스에 그린 장면을 [`promo/render.py`](promo/render.py)가 10ms 단위로 찍어 만든 것입니다.
스프라이트는 정수 2배 확대(nearest-neighbor)로만 그리고 프레임마다 원래 재생 간격을 지키며 동작은 한 사이클이 끝난 뒤에만 바뀝니다.

```bash
pip install playwright pillow imageio-ffmpeg
python -m playwright install chromium
python promo/render.py
```

`promo/index.html`을 브라우저로 열면 같은 장면을 실시간으로도 볼 수 있습니다. (로컬 서버에서 열어야 스프라이트가 불러와집니다. 예: `python -m http.server` 실행 후 `http://localhost:8000/promo/`)

## 저작권 안내

- 이 저장소는 **비공식 팬 제작물**입니다. 공식 애니메이션에서 추출한 모션이 아닙니다.
- 치이카와 캐릭터와 이름, 공식 그림의 권리는 원작자 나가노(ナガノ)와 각 권리자에게 있습니다.
- 캐릭터 스프라이트에는 별도 라이선스를 부여하지 않으며 상업적 이용이나 재판매를 허락하지 않습니다. 개인적으로 즐기는 용도로만 써 주세요.
- 권리자의 요청이 있으면 즉시 내리겠습니다.

---

## English

**Chiikawa Dots Pets** brings Chiikawa, Hachiware and Usagi to the Codex desktop app as animated pets.
Each pet follows the Codex pet v2 sprite format (an 8 × 11 grid of 192 × 208 cells on a 1536 × 2288 transparent PNG) with all nine state animations and a 16-direction look loop.

**Install on Windows (PowerShell)**

```powershell
irm https://raw.githubusercontent.com/heelee912/chiikawa-dots-pets/main/install.ps1 | iex
```

**Install on macOS or Linux**

```bash
curl -fsSL https://raw.githubusercontent.com/heelee912/chiikawa-dots-pets/main/install.sh | sh
```

You can also copy any folder under `pets/` into `~/.codex/pets/` by hand. Restart Codex and pick the pet from its pet list.

This is an unofficial fan project. Chiikawa and all related characters belong to Nagano and their respective rights holders. The sprites carry no license for commercial use or redistribution.
