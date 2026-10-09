<div align="center">

# Chiikawa Dots Pets

**치이카와 친구들 11명을 Codex 데스크톱 펫으로**

[한국어](README.md) · [English](README.en.md) · [日本語](README.ja.md)

<img src="assets/promo-ko.gif" alt="치이카와 친구들 11명이 데스크톱 위에서 작업에 반응하고, 커서를 따라보고, 화면을 뛰어다니는 소개 영상" width="100%">

[고화질 영상 보기 (MP4 · 1080p · 100fps)](assets/promo-ko.mp4) · [릴리즈 다운로드](https://github.com/heelee912/chiikawa-dots-pets/releases/latest)

</div>

---

치이카와 친구들 **11명**을 Codex 데스크톱 앱의 펫으로 데려올 수 있습니다.
모든 펫은 **Codex 펫 v2 규격**(8열 × 11행 · 셀 192 × 208 · 1536 × 2288 투명 PNG)이고, 9가지 상태 모션과 16방향 시선을 갖추고 있습니다.

## 캐릭터

<table>
<tr><td align="center"><img src="assets/motions/chiikawa/idle.gif" width="96" alt="치이카와"><br><sub>치이카와<br><code>chiikawa</code></sub></td><td align="center"><img src="assets/motions/hachiware/idle.gif" width="96" alt="하치와레"><br><sub>하치와레<br><code>hachiware</code></sub></td><td align="center"><img src="assets/motions/usagi/idle.gif" width="96" alt="우사기"><br><sub>우사기<br><code>usagi</code></sub></td><td align="center"><img src="assets/motions/momonga/idle.gif" width="96" alt="모몽가"><br><sub>모몽가<br><code>momonga</code></sub></td><td align="center"><img src="assets/motions/shisa/idle.gif" width="96" alt="시사"><br><sub>시사<br><code>shisa</code></sub></td><td align="center"><img src="assets/motions/rakko/idle.gif" width="96" alt="랏코"><br><sub>랏코<br><code>rakko</code></sub></td></tr>
<tr><td align="center"><img src="assets/motions/kurimanju/idle.gif" width="96" alt="쿠리만주"><br><sub>쿠리만주<br><code>kurimanju</code></sub></td><td align="center"><img src="assets/motions/siren/idle.gif" width="96" alt="세이렌"><br><sub>세이렌<br><code>siren</code></sub></td><td align="center"><img src="assets/motions/furuhonya/idle.gif" width="96" alt="후루혼야"><br><sub>후루혼야<br><code>furuhonya</code></sub></td><td align="center"><img src="assets/motions/anoko/idle.gif" width="96" alt="아노코"><br><sub>아노코<br><code>anoko</code></sub></td><td align="center"><img src="assets/motions/dekatsuyo/idle.gif" width="96" alt="데카츠요"><br><sub>데카츠요<br><code>dekatsuyo</code></sub></td></tr>
</table>

## 설치

### 한 줄 설치

**Windows (PowerShell)**

```powershell
irm https://raw.githubusercontent.com/heelee912/chiikawa-dots-pets/main/install.ps1 | iex
```

**macOS · Linux**

```bash
curl -fsSL https://raw.githubusercontent.com/heelee912/chiikawa-dots-pets/main/install.sh | sh
```

11명 모두 설치됩니다. 일부만 원하면 `CHIIKAWA_PETS` 환경 변수에 펫 ID를 적어 주세요. 설치 후 Codex를 다시 시작하고 펫 목록에서 고르면 됩니다.

```powershell
$env:CHIIKAWA_PETS = "chiikawa,momonga"; irm https://raw.githubusercontent.com/heelee912/chiikawa-dots-pets/main/install.ps1 | iex
```

### 직접 설치

[최신 릴리즈](https://github.com/heelee912/chiikawa-dots-pets/releases/latest)에서 zip을 내려받아 캐릭터 폴더(`pet.json` + `spritesheet.png`)를 `~/.codex/pets/` 아래에 넣으세요. Windows는 `%USERPROFILE%\.codex\pets\`입니다.

## 모션 갤러리

모든 모션은 승인된 원본 그대로이며 프레임마다 기록된 재생 시간을 지킵니다.

<table>
<tr><th></th><th><sub>쉬기</sub></th><th><sub>달리기 →</sub></th><th><sub>달리기 ←</sub></th><th><sub>인사</sub></th><th><sub>점프</sub></th><th><sub>실패</sub></th><th><sub>기다림</sub></th><th><sub>작업</sub></th><th><sub>검토</sub></th><th><sub>16방향</sub></th></tr>
<tr><th><sub>치이카와</sub></th><td><img src="assets/motions/chiikawa/idle.gif" width="72" alt="치이카와 쉬기"></td><td><img src="assets/motions/chiikawa/running-right.gif" width="72" alt="치이카와 달리기 →"></td><td><img src="assets/motions/chiikawa/running-left.gif" width="72" alt="치이카와 달리기 ←"></td><td><img src="assets/motions/chiikawa/waving.gif" width="72" alt="치이카와 인사"></td><td><img src="assets/motions/chiikawa/jumping.gif" width="72" alt="치이카와 점프"></td><td><img src="assets/motions/chiikawa/failed.gif" width="72" alt="치이카와 실패"></td><td><img src="assets/motions/chiikawa/waiting.gif" width="72" alt="치이카와 기다림"></td><td><img src="assets/motions/chiikawa/running.gif" width="72" alt="치이카와 작업"></td><td><img src="assets/motions/chiikawa/review.gif" width="72" alt="치이카와 검토"></td><td><img src="assets/motions/chiikawa/look.gif" width="72" alt="치이카와 16방향"></td></tr>
<tr><th><sub>하치와레</sub></th><td><img src="assets/motions/hachiware/idle.gif" width="72" alt="하치와레 쉬기"></td><td><img src="assets/motions/hachiware/running-right.gif" width="72" alt="하치와레 달리기 →"></td><td><img src="assets/motions/hachiware/running-left.gif" width="72" alt="하치와레 달리기 ←"></td><td><img src="assets/motions/hachiware/waving.gif" width="72" alt="하치와레 인사"></td><td><img src="assets/motions/hachiware/jumping.gif" width="72" alt="하치와레 점프"></td><td><img src="assets/motions/hachiware/failed.gif" width="72" alt="하치와레 실패"></td><td><img src="assets/motions/hachiware/waiting.gif" width="72" alt="하치와레 기다림"></td><td><img src="assets/motions/hachiware/running.gif" width="72" alt="하치와레 작업"></td><td><img src="assets/motions/hachiware/review.gif" width="72" alt="하치와레 검토"></td><td><img src="assets/motions/hachiware/look.gif" width="72" alt="하치와레 16방향"></td></tr>
<tr><th><sub>우사기</sub></th><td><img src="assets/motions/usagi/idle.gif" width="72" alt="우사기 쉬기"></td><td><img src="assets/motions/usagi/running-right.gif" width="72" alt="우사기 달리기 →"></td><td><img src="assets/motions/usagi/running-left.gif" width="72" alt="우사기 달리기 ←"></td><td><img src="assets/motions/usagi/waving.gif" width="72" alt="우사기 인사"></td><td><img src="assets/motions/usagi/jumping.gif" width="72" alt="우사기 점프"></td><td><img src="assets/motions/usagi/failed.gif" width="72" alt="우사기 실패"></td><td><img src="assets/motions/usagi/waiting.gif" width="72" alt="우사기 기다림"></td><td><img src="assets/motions/usagi/running.gif" width="72" alt="우사기 작업"></td><td><img src="assets/motions/usagi/review.gif" width="72" alt="우사기 검토"></td><td><img src="assets/motions/usagi/look.gif" width="72" alt="우사기 16방향"></td></tr>
<tr><th><sub>모몽가</sub></th><td><img src="assets/motions/momonga/idle.gif" width="72" alt="모몽가 쉬기"></td><td><img src="assets/motions/momonga/running-right.gif" width="72" alt="모몽가 달리기 →"></td><td><img src="assets/motions/momonga/running-left.gif" width="72" alt="모몽가 달리기 ←"></td><td><img src="assets/motions/momonga/waving.gif" width="72" alt="모몽가 인사"></td><td><img src="assets/motions/momonga/jumping.gif" width="72" alt="모몽가 점프"></td><td><img src="assets/motions/momonga/failed.gif" width="72" alt="모몽가 실패"></td><td><img src="assets/motions/momonga/waiting.gif" width="72" alt="모몽가 기다림"></td><td><img src="assets/motions/momonga/running.gif" width="72" alt="모몽가 작업"></td><td><img src="assets/motions/momonga/review.gif" width="72" alt="모몽가 검토"></td><td><img src="assets/motions/momonga/look.gif" width="72" alt="모몽가 16방향"></td></tr>
<tr><th><sub>시사</sub></th><td><img src="assets/motions/shisa/idle.gif" width="72" alt="시사 쉬기"></td><td><img src="assets/motions/shisa/running-right.gif" width="72" alt="시사 달리기 →"></td><td><img src="assets/motions/shisa/running-left.gif" width="72" alt="시사 달리기 ←"></td><td><img src="assets/motions/shisa/waving.gif" width="72" alt="시사 인사"></td><td><img src="assets/motions/shisa/jumping.gif" width="72" alt="시사 점프"></td><td><img src="assets/motions/shisa/failed.gif" width="72" alt="시사 실패"></td><td><img src="assets/motions/shisa/waiting.gif" width="72" alt="시사 기다림"></td><td><img src="assets/motions/shisa/running.gif" width="72" alt="시사 작업"></td><td><img src="assets/motions/shisa/review.gif" width="72" alt="시사 검토"></td><td><img src="assets/motions/shisa/look.gif" width="72" alt="시사 16방향"></td></tr>
<tr><th><sub>랏코</sub></th><td><img src="assets/motions/rakko/idle.gif" width="72" alt="랏코 쉬기"></td><td><img src="assets/motions/rakko/running-right.gif" width="72" alt="랏코 달리기 →"></td><td><img src="assets/motions/rakko/running-left.gif" width="72" alt="랏코 달리기 ←"></td><td><img src="assets/motions/rakko/waving.gif" width="72" alt="랏코 인사"></td><td><img src="assets/motions/rakko/jumping.gif" width="72" alt="랏코 점프"></td><td><img src="assets/motions/rakko/failed.gif" width="72" alt="랏코 실패"></td><td><img src="assets/motions/rakko/waiting.gif" width="72" alt="랏코 기다림"></td><td><img src="assets/motions/rakko/running.gif" width="72" alt="랏코 작업"></td><td><img src="assets/motions/rakko/review.gif" width="72" alt="랏코 검토"></td><td><img src="assets/motions/rakko/look.gif" width="72" alt="랏코 16방향"></td></tr>
<tr><th><sub>쿠리만주</sub></th><td><img src="assets/motions/kurimanju/idle.gif" width="72" alt="쿠리만주 쉬기"></td><td><img src="assets/motions/kurimanju/running-right.gif" width="72" alt="쿠리만주 달리기 →"></td><td><img src="assets/motions/kurimanju/running-left.gif" width="72" alt="쿠리만주 달리기 ←"></td><td><img src="assets/motions/kurimanju/waving.gif" width="72" alt="쿠리만주 인사"></td><td><img src="assets/motions/kurimanju/jumping.gif" width="72" alt="쿠리만주 점프"></td><td><img src="assets/motions/kurimanju/failed.gif" width="72" alt="쿠리만주 실패"></td><td><img src="assets/motions/kurimanju/waiting.gif" width="72" alt="쿠리만주 기다림"></td><td><img src="assets/motions/kurimanju/running.gif" width="72" alt="쿠리만주 작업"></td><td><img src="assets/motions/kurimanju/review.gif" width="72" alt="쿠리만주 검토"></td><td><img src="assets/motions/kurimanju/look.gif" width="72" alt="쿠리만주 16방향"></td></tr>
<tr><th><sub>세이렌</sub></th><td><img src="assets/motions/siren/idle.gif" width="72" alt="세이렌 쉬기"></td><td><img src="assets/motions/siren/running-right.gif" width="72" alt="세이렌 달리기 →"></td><td><img src="assets/motions/siren/running-left.gif" width="72" alt="세이렌 달리기 ←"></td><td><img src="assets/motions/siren/waving.gif" width="72" alt="세이렌 인사"></td><td><img src="assets/motions/siren/jumping.gif" width="72" alt="세이렌 점프"></td><td><img src="assets/motions/siren/failed.gif" width="72" alt="세이렌 실패"></td><td><img src="assets/motions/siren/waiting.gif" width="72" alt="세이렌 기다림"></td><td><img src="assets/motions/siren/running.gif" width="72" alt="세이렌 작업"></td><td><img src="assets/motions/siren/review.gif" width="72" alt="세이렌 검토"></td><td><img src="assets/motions/siren/look.gif" width="72" alt="세이렌 16방향"></td></tr>
<tr><th><sub>후루혼야</sub></th><td><img src="assets/motions/furuhonya/idle.gif" width="72" alt="후루혼야 쉬기"></td><td><img src="assets/motions/furuhonya/running-right.gif" width="72" alt="후루혼야 달리기 →"></td><td><img src="assets/motions/furuhonya/running-left.gif" width="72" alt="후루혼야 달리기 ←"></td><td><img src="assets/motions/furuhonya/waving.gif" width="72" alt="후루혼야 인사"></td><td><img src="assets/motions/furuhonya/jumping.gif" width="72" alt="후루혼야 점프"></td><td><img src="assets/motions/furuhonya/failed.gif" width="72" alt="후루혼야 실패"></td><td><img src="assets/motions/furuhonya/waiting.gif" width="72" alt="후루혼야 기다림"></td><td><img src="assets/motions/furuhonya/running.gif" width="72" alt="후루혼야 작업"></td><td><img src="assets/motions/furuhonya/review.gif" width="72" alt="후루혼야 검토"></td><td><img src="assets/motions/furuhonya/look.gif" width="72" alt="후루혼야 16방향"></td></tr>
<tr><th><sub>아노코</sub></th><td><img src="assets/motions/anoko/idle.gif" width="72" alt="아노코 쉬기"></td><td><img src="assets/motions/anoko/running-right.gif" width="72" alt="아노코 달리기 →"></td><td><img src="assets/motions/anoko/running-left.gif" width="72" alt="아노코 달리기 ←"></td><td><img src="assets/motions/anoko/waving.gif" width="72" alt="아노코 인사"></td><td><img src="assets/motions/anoko/jumping.gif" width="72" alt="아노코 점프"></td><td><img src="assets/motions/anoko/failed.gif" width="72" alt="아노코 실패"></td><td><img src="assets/motions/anoko/waiting.gif" width="72" alt="아노코 기다림"></td><td><img src="assets/motions/anoko/running.gif" width="72" alt="아노코 작업"></td><td><img src="assets/motions/anoko/review.gif" width="72" alt="아노코 검토"></td><td><img src="assets/motions/anoko/look.gif" width="72" alt="아노코 16방향"></td></tr>
<tr><th><sub>데카츠요</sub></th><td><img src="assets/motions/dekatsuyo/idle.gif" width="72" alt="데카츠요 쉬기"></td><td><img src="assets/motions/dekatsuyo/running-right.gif" width="72" alt="데카츠요 달리기 →"></td><td><img src="assets/motions/dekatsuyo/running-left.gif" width="72" alt="데카츠요 달리기 ←"></td><td><img src="assets/motions/dekatsuyo/waving.gif" width="72" alt="데카츠요 인사"></td><td><img src="assets/motions/dekatsuyo/jumping.gif" width="72" alt="데카츠요 점프"></td><td><img src="assets/motions/dekatsuyo/failed.gif" width="72" alt="데카츠요 실패"></td><td><img src="assets/motions/dekatsuyo/waiting.gif" width="72" alt="데카츠요 기다림"></td><td><img src="assets/motions/dekatsuyo/running.gif" width="72" alt="데카츠요 작업"></td><td><img src="assets/motions/dekatsuyo/review.gif" width="72" alt="데카츠요 검토"></td><td><img src="assets/motions/dekatsuyo/look.gif" width="72" alt="데카츠요 16방향"></td></tr>
</table>

> Codex 상태 이름 `running`은 작업 중이라는 뜻이라 여기서는 **작업** 모션입니다. 화면을 달리는 모션은 `running-right`와 `running-left`입니다.

<details>
<summary>스프라이트 규격</summary>

| 행 | 상태 | 프레임 |
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
| 9 – 10 | 시선 16방향 (12시부터 시계 방향) | 16 |

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

## 저작권 안내

이 저장소는 비공식 팬 제작물입니다. 치이카와 캐릭터와 이름의 권리는 원작자 나가노(ナガノ)와 각 권리자에게 있습니다. 상업적 이용과 재배포를 허락하지 않으며, 권리자의 요청이 있으면 즉시 내리겠습니다.
