<div align="center">

# Chiikawa Dots Pets

**치이카와 친구들 11명을 Codex 데스크톱 펫으로 · Eleven Chiikawa friends as Codex desktop pets · ちいかわの仲間11人をCodexのデスクトップペットに**

[한국어](#한국어) · [English](#english) · [日本語](#日本語) · [Releases](https://github.com/heelee912/chiikawa-dots-pets/releases/latest)

</div>

---

## 한국어

<div align="center">
<img src="assets/promo-ko.gif" alt="치이카와 친구들 11명이 단체 사진으로 등장해 달리고 Codex 상태별 모션을 보여 주는 소개 영상" width="100%">

[고화질 영상 보기 (MP4 · 1080p 100fps)](assets/promo-ko.mp4)
</div>

치이카와 친구들 **11명**을 Codex 데스크톱 앱의 펫으로 데려올 수 있습니다.
모든 펫은 **Codex 펫 v2 규격**(8열 × 11행 · 셀 192 × 208 · 1536 × 2288 투명 PNG)이고, 9가지 상태 모션과 16방향 시선을 갖추고 있습니다.

<table>
<tr><td align="center"><img src="assets/motions/chiikawa/idle.gif" width="96" alt="치이카와"><br><sub>치이카와<br><code>chiikawa</code></sub></td><td align="center"><img src="assets/motions/hachiware/idle.gif" width="96" alt="하치와레"><br><sub>하치와레<br><code>hachiware</code></sub></td><td align="center"><img src="assets/motions/usagi/idle.gif" width="96" alt="우사기"><br><sub>우사기<br><code>usagi</code></sub></td><td align="center"><img src="assets/motions/momonga/idle.gif" width="96" alt="모몽가"><br><sub>모몽가<br><code>momonga</code></sub></td><td align="center"><img src="assets/motions/shisa/idle.gif" width="96" alt="시사"><br><sub>시사<br><code>shisa</code></sub></td><td align="center"><img src="assets/motions/rakko/idle.gif" width="96" alt="랏코"><br><sub>랏코<br><code>rakko</code></sub></td></tr>
<tr><td align="center"><img src="assets/motions/kurimanju/idle.gif" width="96" alt="쿠리만주"><br><sub>쿠리만주<br><code>kurimanju</code></sub></td><td align="center"><img src="assets/motions/siren/idle.gif" width="96" alt="세이렌"><br><sub>세이렌<br><code>siren</code></sub></td><td align="center"><img src="assets/motions/furuhonya/idle.gif" width="96" alt="후루혼야"><br><sub>후루혼야<br><code>furuhonya</code></sub></td><td align="center"><img src="assets/motions/anoko/idle.gif" width="96" alt="아노코"><br><sub>아노코<br><code>anoko</code></sub></td><td align="center"><img src="assets/motions/dekatsuyo/idle.gif" width="96" alt="데카츠요"><br><sub>데카츠요<br><code>dekatsuyo</code></sub></td></tr>
</table>

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

> 모든 모션은 승인된 원본 그대로이며 프레임마다 기록된 재생 시간을 지킵니다. 전체 모션은 아래 [모션 갤러리](#모션-갤러리--motion-gallery--モーション一覧)에서 볼 수 있습니다.

**저작권 안내:** 이 저장소는 비공식 팬 제작물입니다. 치이카와 캐릭터와 이름의 권리는 원작자 나가노(ナガノ)와 각 권리자에게 있습니다. 상업적 이용과 재배포를 허락하지 않으며, 권리자의 요청이 있으면 즉시 내리겠습니다.

---

## English

<div align="center">
<img src="assets/promo-en.gif" alt="Eleven Chiikawa friends gather for a group photo, run, and react to each Codex state" width="100%">

[Watch in full quality (MP4 · 1080p 100fps)](assets/promo-en.mp4)
</div>

Bring **eleven** Chiikawa friends to the Codex desktop app as animated pets.
Every pet follows the **Codex pet v2 format** (an 8 × 11 grid of 192 × 208 cells on a 1536 × 2288 transparent PNG) with nine state animations and a 16-direction look loop.

<table>
<tr><td align="center"><img src="assets/motions/chiikawa/idle.gif" width="96" alt="Chiikawa"><br><sub>Chiikawa<br><code>chiikawa</code></sub></td><td align="center"><img src="assets/motions/hachiware/idle.gif" width="96" alt="Hachiware"><br><sub>Hachiware<br><code>hachiware</code></sub></td><td align="center"><img src="assets/motions/usagi/idle.gif" width="96" alt="Usagi"><br><sub>Usagi<br><code>usagi</code></sub></td><td align="center"><img src="assets/motions/momonga/idle.gif" width="96" alt="Momonga"><br><sub>Momonga<br><code>momonga</code></sub></td><td align="center"><img src="assets/motions/shisa/idle.gif" width="96" alt="Shisa"><br><sub>Shisa<br><code>shisa</code></sub></td><td align="center"><img src="assets/motions/rakko/idle.gif" width="96" alt="Rakko"><br><sub>Rakko<br><code>rakko</code></sub></td></tr>
<tr><td align="center"><img src="assets/motions/kurimanju/idle.gif" width="96" alt="Kurimanju"><br><sub>Kurimanju<br><code>kurimanju</code></sub></td><td align="center"><img src="assets/motions/siren/idle.gif" width="96" alt="Siren"><br><sub>Siren<br><code>siren</code></sub></td><td align="center"><img src="assets/motions/furuhonya/idle.gif" width="96" alt="Furuhonya"><br><sub>Furuhonya<br><code>furuhonya</code></sub></td><td align="center"><img src="assets/motions/anoko/idle.gif" width="96" alt="Anoko"><br><sub>Anoko<br><code>anoko</code></sub></td><td align="center"><img src="assets/motions/dekatsuyo/idle.gif" width="96" alt="Dekatsuyo"><br><sub>Dekatsuyo<br><code>dekatsuyo</code></sub></td></tr>
</table>

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

> Every motion is the approved original and keeps its recorded frame timing. See the full set in the [motion gallery](#모션-갤러리--motion-gallery--モーション一覧) below.

**Notice:** This is an unofficial fan project. Chiikawa and all related characters belong to Nagano and their respective rights holders. The sprites carry no license for commercial use or redistribution, and they will be taken down on request.

---

## 日本語

<div align="center">
<img src="assets/promo-ja.gif" alt="ちいかわの仲間11人が集合写真で登場し、走ってCodexの状態ごとの動きを見せる紹介動画" width="100%">

[高画質で見る（MP4 · 1080p 100fps）](assets/promo-ja.mp4)
</div>

ちいかわの仲間**11人**を、Codexデスクトップアプリのペットとして連れてこられます。
すべてのペットは **Codexペット v2 形式**（8列 × 11行 · セル 192 × 208 · 1536 × 2288 の透過PNG）で、9種類の状態モーションと16方向の視線を備えています。

<table>
<tr><td align="center"><img src="assets/motions/chiikawa/idle.gif" width="96" alt="ちいかわ"><br><sub>ちいかわ<br><code>chiikawa</code></sub></td><td align="center"><img src="assets/motions/hachiware/idle.gif" width="96" alt="ハチワレ"><br><sub>ハチワレ<br><code>hachiware</code></sub></td><td align="center"><img src="assets/motions/usagi/idle.gif" width="96" alt="うさぎ"><br><sub>うさぎ<br><code>usagi</code></sub></td><td align="center"><img src="assets/motions/momonga/idle.gif" width="96" alt="モモンガ"><br><sub>モモンガ<br><code>momonga</code></sub></td><td align="center"><img src="assets/motions/shisa/idle.gif" width="96" alt="シーサー"><br><sub>シーサー<br><code>shisa</code></sub></td><td align="center"><img src="assets/motions/rakko/idle.gif" width="96" alt="ラッコ"><br><sub>ラッコ<br><code>rakko</code></sub></td></tr>
<tr><td align="center"><img src="assets/motions/kurimanju/idle.gif" width="96" alt="くりまんじゅう"><br><sub>くりまんじゅう<br><code>kurimanju</code></sub></td><td align="center"><img src="assets/motions/siren/idle.gif" width="96" alt="セイレーン"><br><sub>セイレーン<br><code>siren</code></sub></td><td align="center"><img src="assets/motions/furuhonya/idle.gif" width="96" alt="古本屋"><br><sub>古本屋<br><code>furuhonya</code></sub></td><td align="center"><img src="assets/motions/anoko/idle.gif" width="96" alt="あのこ"><br><sub>あのこ<br><code>anoko</code></sub></td><td align="center"><img src="assets/motions/dekatsuyo/idle.gif" width="96" alt="でかつよ"><br><sub>でかつよ<br><code>dekatsuyo</code></sub></td></tr>
</table>

### ワンライナーでインストール

**Windows (PowerShell)**

```powershell
irm https://raw.githubusercontent.com/heelee912/chiikawa-dots-pets/main/install.ps1 | iex
```

**macOS · Linux**

```bash
curl -fsSL https://raw.githubusercontent.com/heelee912/chiikawa-dots-pets/main/install.sh | sh
```

11体すべてがインストールされます。一部だけ入れたいときは `CHIIKAWA_PETS` にペットIDを指定してください。インストール後にCodexを再起動し、ペット一覧から選んでください。

```powershell
$env:CHIIKAWA_PETS = "chiikawa,momonga"; irm https://raw.githubusercontent.com/heelee912/chiikawa-dots-pets/main/install.ps1 | iex
```

### 手動インストール

[最新リリース](https://github.com/heelee912/chiikawa-dots-pets/releases/latest)からzipをダウンロードし、各ペットのフォルダ（`pet.json` + `spritesheet.png`）を `~/.codex/pets/` に置いてください。Windowsでは `%USERPROFILE%\.codex\pets\` です。

> すべてのモーションは承認済みのオリジナルそのままで、記録されたフレームの再生時間を守っています。全モーションは下の[モーション一覧](#모션-갤러리--motion-gallery--モーション一覧)で見られます。

**ご注意:** このリポジトリは非公式のファンメイドです。ちいかわのキャラクターと名称の権利は、原作者ナガノ氏および各権利者に帰属します。商用利用や再配布は許可していません。権利者からのご要望があれば、すぐに取り下げます。

---

## 모션 갤러리 · Motion gallery · モーション一覧

<table>
<tr><th></th><th><sub>쉬기<br>Idle<br>待機</sub></th><th><sub>달리기 →<br>Run →<br>走る →</sub></th><th><sub>달리기 ←<br>Run ←<br>走る ←</sub></th><th><sub>인사<br>Wave<br>あいさつ</sub></th><th><sub>점프<br>Jump<br>ジャンプ</sub></th><th><sub>실패<br>Failed<br>失敗</sub></th><th><sub>기다림<br>Waiting<br>待つ</sub></th><th><sub>작업<br>Working<br>作業</sub></th><th><sub>검토<br>Review<br>レビュー</sub></th><th><sub>16방향<br>16-way look<br>16方向</sub></th></tr>
<tr><th><sub>치이카와<br>Chiikawa<br>ちいかわ</sub></th><td><img src="assets/motions/chiikawa/idle.gif" width="72" alt="Chiikawa Idle"></td><td><img src="assets/motions/chiikawa/running-right.gif" width="72" alt="Chiikawa Run →"></td><td><img src="assets/motions/chiikawa/running-left.gif" width="72" alt="Chiikawa Run ←"></td><td><img src="assets/motions/chiikawa/waving.gif" width="72" alt="Chiikawa Wave"></td><td><img src="assets/motions/chiikawa/jumping.gif" width="72" alt="Chiikawa Jump"></td><td><img src="assets/motions/chiikawa/failed.gif" width="72" alt="Chiikawa Failed"></td><td><img src="assets/motions/chiikawa/waiting.gif" width="72" alt="Chiikawa Waiting"></td><td><img src="assets/motions/chiikawa/running.gif" width="72" alt="Chiikawa Working"></td><td><img src="assets/motions/chiikawa/review.gif" width="72" alt="Chiikawa Review"></td><td><img src="assets/motions/chiikawa/look.gif" width="72" alt="Chiikawa 16-way look"></td></tr>
<tr><th><sub>하치와레<br>Hachiware<br>ハチワレ</sub></th><td><img src="assets/motions/hachiware/idle.gif" width="72" alt="Hachiware Idle"></td><td><img src="assets/motions/hachiware/running-right.gif" width="72" alt="Hachiware Run →"></td><td><img src="assets/motions/hachiware/running-left.gif" width="72" alt="Hachiware Run ←"></td><td><img src="assets/motions/hachiware/waving.gif" width="72" alt="Hachiware Wave"></td><td><img src="assets/motions/hachiware/jumping.gif" width="72" alt="Hachiware Jump"></td><td><img src="assets/motions/hachiware/failed.gif" width="72" alt="Hachiware Failed"></td><td><img src="assets/motions/hachiware/waiting.gif" width="72" alt="Hachiware Waiting"></td><td><img src="assets/motions/hachiware/running.gif" width="72" alt="Hachiware Working"></td><td><img src="assets/motions/hachiware/review.gif" width="72" alt="Hachiware Review"></td><td><img src="assets/motions/hachiware/look.gif" width="72" alt="Hachiware 16-way look"></td></tr>
<tr><th><sub>우사기<br>Usagi<br>うさぎ</sub></th><td><img src="assets/motions/usagi/idle.gif" width="72" alt="Usagi Idle"></td><td><img src="assets/motions/usagi/running-right.gif" width="72" alt="Usagi Run →"></td><td><img src="assets/motions/usagi/running-left.gif" width="72" alt="Usagi Run ←"></td><td><img src="assets/motions/usagi/waving.gif" width="72" alt="Usagi Wave"></td><td><img src="assets/motions/usagi/jumping.gif" width="72" alt="Usagi Jump"></td><td><img src="assets/motions/usagi/failed.gif" width="72" alt="Usagi Failed"></td><td><img src="assets/motions/usagi/waiting.gif" width="72" alt="Usagi Waiting"></td><td><img src="assets/motions/usagi/running.gif" width="72" alt="Usagi Working"></td><td><img src="assets/motions/usagi/review.gif" width="72" alt="Usagi Review"></td><td><img src="assets/motions/usagi/look.gif" width="72" alt="Usagi 16-way look"></td></tr>
<tr><th><sub>모몽가<br>Momonga<br>モモンガ</sub></th><td><img src="assets/motions/momonga/idle.gif" width="72" alt="Momonga Idle"></td><td><img src="assets/motions/momonga/running-right.gif" width="72" alt="Momonga Run →"></td><td><img src="assets/motions/momonga/running-left.gif" width="72" alt="Momonga Run ←"></td><td><img src="assets/motions/momonga/waving.gif" width="72" alt="Momonga Wave"></td><td><img src="assets/motions/momonga/jumping.gif" width="72" alt="Momonga Jump"></td><td><img src="assets/motions/momonga/failed.gif" width="72" alt="Momonga Failed"></td><td><img src="assets/motions/momonga/waiting.gif" width="72" alt="Momonga Waiting"></td><td><img src="assets/motions/momonga/running.gif" width="72" alt="Momonga Working"></td><td><img src="assets/motions/momonga/review.gif" width="72" alt="Momonga Review"></td><td><img src="assets/motions/momonga/look.gif" width="72" alt="Momonga 16-way look"></td></tr>
<tr><th><sub>시사<br>Shisa<br>シーサー</sub></th><td><img src="assets/motions/shisa/idle.gif" width="72" alt="Shisa Idle"></td><td><img src="assets/motions/shisa/running-right.gif" width="72" alt="Shisa Run →"></td><td><img src="assets/motions/shisa/running-left.gif" width="72" alt="Shisa Run ←"></td><td><img src="assets/motions/shisa/waving.gif" width="72" alt="Shisa Wave"></td><td><img src="assets/motions/shisa/jumping.gif" width="72" alt="Shisa Jump"></td><td><img src="assets/motions/shisa/failed.gif" width="72" alt="Shisa Failed"></td><td><img src="assets/motions/shisa/waiting.gif" width="72" alt="Shisa Waiting"></td><td><img src="assets/motions/shisa/running.gif" width="72" alt="Shisa Working"></td><td><img src="assets/motions/shisa/review.gif" width="72" alt="Shisa Review"></td><td><img src="assets/motions/shisa/look.gif" width="72" alt="Shisa 16-way look"></td></tr>
<tr><th><sub>랏코<br>Rakko<br>ラッコ</sub></th><td><img src="assets/motions/rakko/idle.gif" width="72" alt="Rakko Idle"></td><td><img src="assets/motions/rakko/running-right.gif" width="72" alt="Rakko Run →"></td><td><img src="assets/motions/rakko/running-left.gif" width="72" alt="Rakko Run ←"></td><td><img src="assets/motions/rakko/waving.gif" width="72" alt="Rakko Wave"></td><td><img src="assets/motions/rakko/jumping.gif" width="72" alt="Rakko Jump"></td><td><img src="assets/motions/rakko/failed.gif" width="72" alt="Rakko Failed"></td><td><img src="assets/motions/rakko/waiting.gif" width="72" alt="Rakko Waiting"></td><td><img src="assets/motions/rakko/running.gif" width="72" alt="Rakko Working"></td><td><img src="assets/motions/rakko/review.gif" width="72" alt="Rakko Review"></td><td><img src="assets/motions/rakko/look.gif" width="72" alt="Rakko 16-way look"></td></tr>
<tr><th><sub>쿠리만주<br>Kurimanju<br>くりまんじゅう</sub></th><td><img src="assets/motions/kurimanju/idle.gif" width="72" alt="Kurimanju Idle"></td><td><img src="assets/motions/kurimanju/running-right.gif" width="72" alt="Kurimanju Run →"></td><td><img src="assets/motions/kurimanju/running-left.gif" width="72" alt="Kurimanju Run ←"></td><td><img src="assets/motions/kurimanju/waving.gif" width="72" alt="Kurimanju Wave"></td><td><img src="assets/motions/kurimanju/jumping.gif" width="72" alt="Kurimanju Jump"></td><td><img src="assets/motions/kurimanju/failed.gif" width="72" alt="Kurimanju Failed"></td><td><img src="assets/motions/kurimanju/waiting.gif" width="72" alt="Kurimanju Waiting"></td><td><img src="assets/motions/kurimanju/running.gif" width="72" alt="Kurimanju Working"></td><td><img src="assets/motions/kurimanju/review.gif" width="72" alt="Kurimanju Review"></td><td><img src="assets/motions/kurimanju/look.gif" width="72" alt="Kurimanju 16-way look"></td></tr>
<tr><th><sub>세이렌<br>Siren<br>セイレーン</sub></th><td><img src="assets/motions/siren/idle.gif" width="72" alt="Siren Idle"></td><td><img src="assets/motions/siren/running-right.gif" width="72" alt="Siren Run →"></td><td><img src="assets/motions/siren/running-left.gif" width="72" alt="Siren Run ←"></td><td><img src="assets/motions/siren/waving.gif" width="72" alt="Siren Wave"></td><td><img src="assets/motions/siren/jumping.gif" width="72" alt="Siren Jump"></td><td><img src="assets/motions/siren/failed.gif" width="72" alt="Siren Failed"></td><td><img src="assets/motions/siren/waiting.gif" width="72" alt="Siren Waiting"></td><td><img src="assets/motions/siren/running.gif" width="72" alt="Siren Working"></td><td><img src="assets/motions/siren/review.gif" width="72" alt="Siren Review"></td><td><img src="assets/motions/siren/look.gif" width="72" alt="Siren 16-way look"></td></tr>
<tr><th><sub>후루혼야<br>Furuhonya<br>古本屋</sub></th><td><img src="assets/motions/furuhonya/idle.gif" width="72" alt="Furuhonya Idle"></td><td><img src="assets/motions/furuhonya/running-right.gif" width="72" alt="Furuhonya Run →"></td><td><img src="assets/motions/furuhonya/running-left.gif" width="72" alt="Furuhonya Run ←"></td><td><img src="assets/motions/furuhonya/waving.gif" width="72" alt="Furuhonya Wave"></td><td><img src="assets/motions/furuhonya/jumping.gif" width="72" alt="Furuhonya Jump"></td><td><img src="assets/motions/furuhonya/failed.gif" width="72" alt="Furuhonya Failed"></td><td><img src="assets/motions/furuhonya/waiting.gif" width="72" alt="Furuhonya Waiting"></td><td><img src="assets/motions/furuhonya/running.gif" width="72" alt="Furuhonya Working"></td><td><img src="assets/motions/furuhonya/review.gif" width="72" alt="Furuhonya Review"></td><td><img src="assets/motions/furuhonya/look.gif" width="72" alt="Furuhonya 16-way look"></td></tr>
<tr><th><sub>아노코<br>Anoko<br>あのこ</sub></th><td><img src="assets/motions/anoko/idle.gif" width="72" alt="Anoko Idle"></td><td><img src="assets/motions/anoko/running-right.gif" width="72" alt="Anoko Run →"></td><td><img src="assets/motions/anoko/running-left.gif" width="72" alt="Anoko Run ←"></td><td><img src="assets/motions/anoko/waving.gif" width="72" alt="Anoko Wave"></td><td><img src="assets/motions/anoko/jumping.gif" width="72" alt="Anoko Jump"></td><td><img src="assets/motions/anoko/failed.gif" width="72" alt="Anoko Failed"></td><td><img src="assets/motions/anoko/waiting.gif" width="72" alt="Anoko Waiting"></td><td><img src="assets/motions/anoko/running.gif" width="72" alt="Anoko Working"></td><td><img src="assets/motions/anoko/review.gif" width="72" alt="Anoko Review"></td><td><img src="assets/motions/anoko/look.gif" width="72" alt="Anoko 16-way look"></td></tr>
<tr><th><sub>데카츠요<br>Dekatsuyo<br>でかつよ</sub></th><td><img src="assets/motions/dekatsuyo/idle.gif" width="72" alt="Dekatsuyo Idle"></td><td><img src="assets/motions/dekatsuyo/running-right.gif" width="72" alt="Dekatsuyo Run →"></td><td><img src="assets/motions/dekatsuyo/running-left.gif" width="72" alt="Dekatsuyo Run ←"></td><td><img src="assets/motions/dekatsuyo/waving.gif" width="72" alt="Dekatsuyo Wave"></td><td><img src="assets/motions/dekatsuyo/jumping.gif" width="72" alt="Dekatsuyo Jump"></td><td><img src="assets/motions/dekatsuyo/failed.gif" width="72" alt="Dekatsuyo Failed"></td><td><img src="assets/motions/dekatsuyo/waiting.gif" width="72" alt="Dekatsuyo Waiting"></td><td><img src="assets/motions/dekatsuyo/running.gif" width="72" alt="Dekatsuyo Working"></td><td><img src="assets/motions/dekatsuyo/review.gif" width="72" alt="Dekatsuyo Review"></td><td><img src="assets/motions/dekatsuyo/look.gif" width="72" alt="Dekatsuyo 16-way look"></td></tr>
</table>

<details>
<summary>스프라이트 규격 · Sprite format · スプライト仕様</summary>

| Row | State | Frames |
|:-:|:--|:-:|
| 0 | idle | 6 |
| 1 | running-right | 8 |
| 2 | running-left | 8 |
| 3 | waving | 4 |
| 4 | jumping | 5 |
| 5 | failed | 8 |
| 6 | waiting | 6 |
| 7 | running (busy working) | 6 |
| 8 | review | 6 |
| 9 – 10 | look, 16 directions clockwise from 12 o'clock | 16 |

`pet.json`:

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

## 영상 다시 만들기 · Rebuilding the promo · 動画の再生成

[`promo/index.html`](promo/index.html) draws the movie from the real spritesheets and [`promo/cast.json`](promo/cast.json), which holds each pet's recorded frame timing. [`promo/render.py`](promo/render.py) steps its clock in 10 ms and writes the MP4, the README GIF and a poster for each language.

```bash
pip install playwright pillow numpy imageio-ffmpeg
python -m playwright install chromium
python promo/render.py --lang ko   # or en, ja
```
