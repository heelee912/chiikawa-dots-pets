<div align="center">

# Chiikawa Dots Pets

**ちいかわの仲間11人をCodexのデスクトップペットに**

[한국어](README.md) · [English](README.en.md) · [日本語](README.ja.md)

<img src="assets/promo-ja.gif" alt="ちいかわの仲間11人がウィンドウの横で作業に反応し、画面の真ん中へ走ってきてカーソルを目で追い、みんなでジャンプする紹介動画" width="100%">

[高画質で見る（MP4 · 1080p · 100fps）](assets/promo-ja.mp4) · [リリースをダウンロード](https://github.com/heelee912/chiikawa-dots-pets/releases/latest)

</div>

---

ちいかわの仲間**11人**を、Codexデスクトップアプリのペットとして連れてこられます。
すべてのペットは **Codexペット v2 形式**（8列 × 11行 · セル 192 × 208 · 1536 × 2288 の透過PNG）で、9種類の状態モーションと16方向の視線を備えています。

## キャラクター

<table>
<tr><td align="center"><img src="assets/motions/chiikawa/idle.gif" width="96" alt="ちいかわ"><br><sub>ちいかわ<br><code>chiikawa</code></sub></td><td align="center"><img src="assets/motions/hachiware/idle.gif" width="96" alt="ハチワレ"><br><sub>ハチワレ<br><code>hachiware</code></sub></td><td align="center"><img src="assets/motions/usagi/idle.gif" width="96" alt="うさぎ"><br><sub>うさぎ<br><code>usagi</code></sub></td><td align="center"><img src="assets/motions/momonga/idle.gif" width="96" alt="モモンガ"><br><sub>モモンガ<br><code>momonga</code></sub></td><td align="center"><img src="assets/motions/shisa/idle.gif" width="96" alt="シーサー"><br><sub>シーサー<br><code>shisa</code></sub></td><td align="center"><img src="assets/motions/rakko/idle.gif" width="96" alt="ラッコ"><br><sub>ラッコ<br><code>rakko</code></sub></td></tr>
<tr><td align="center"><img src="assets/motions/kurimanju/idle.gif" width="96" alt="くりまんじゅう"><br><sub>くりまんじゅう<br><code>kurimanju</code></sub></td><td align="center"><img src="assets/motions/siren/idle.gif" width="96" alt="セイレーン"><br><sub>セイレーン<br><code>siren</code></sub></td><td align="center"><img src="assets/motions/furuhonya/idle.gif" width="96" alt="古本屋"><br><sub>古本屋<br><code>furuhonya</code></sub></td><td align="center"><img src="assets/motions/anoko/idle.gif" width="96" alt="あのこ"><br><sub>あのこ<br><code>anoko</code></sub></td><td align="center"><img src="assets/motions/dekatsuyo/idle.gif" width="96" alt="でかつよ"><br><sub>でかつよ<br><code>dekatsuyo</code></sub></td></tr>
</table>

## インストール

### ワンライナー

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

## モーション一覧

すべてのモーションは承認済みのオリジナルそのままで、記録されたフレームの再生時間を守っています。

<table>
<tr><th></th><th><sub>待機</sub></th><th><sub>走る →</sub></th><th><sub>走る ←</sub></th><th><sub>あいさつ</sub></th><th><sub>ジャンプ</sub></th><th><sub>失敗</sub></th><th><sub>待つ</sub></th><th><sub>作業</sub></th><th><sub>レビュー</sub></th><th><sub>16方向</sub></th></tr>
<tr><th><sub>ちいかわ</sub></th><td><img src="assets/motions/chiikawa/idle.gif" width="72" alt="ちいかわ 待機"></td><td><img src="assets/motions/chiikawa/running-right.gif" width="72" alt="ちいかわ 走る →"></td><td><img src="assets/motions/chiikawa/running-left.gif" width="72" alt="ちいかわ 走る ←"></td><td><img src="assets/motions/chiikawa/waving.gif" width="72" alt="ちいかわ あいさつ"></td><td><img src="assets/motions/chiikawa/jumping.gif" width="72" alt="ちいかわ ジャンプ"></td><td><img src="assets/motions/chiikawa/failed.gif" width="72" alt="ちいかわ 失敗"></td><td><img src="assets/motions/chiikawa/waiting.gif" width="72" alt="ちいかわ 待つ"></td><td><img src="assets/motions/chiikawa/running.gif" width="72" alt="ちいかわ 作業"></td><td><img src="assets/motions/chiikawa/review.gif" width="72" alt="ちいかわ レビュー"></td><td><img src="assets/motions/chiikawa/look.gif" width="72" alt="ちいかわ 16方向"></td></tr>
<tr><th><sub>ハチワレ</sub></th><td><img src="assets/motions/hachiware/idle.gif" width="72" alt="ハチワレ 待機"></td><td><img src="assets/motions/hachiware/running-right.gif" width="72" alt="ハチワレ 走る →"></td><td><img src="assets/motions/hachiware/running-left.gif" width="72" alt="ハチワレ 走る ←"></td><td><img src="assets/motions/hachiware/waving.gif" width="72" alt="ハチワレ あいさつ"></td><td><img src="assets/motions/hachiware/jumping.gif" width="72" alt="ハチワレ ジャンプ"></td><td><img src="assets/motions/hachiware/failed.gif" width="72" alt="ハチワレ 失敗"></td><td><img src="assets/motions/hachiware/waiting.gif" width="72" alt="ハチワレ 待つ"></td><td><img src="assets/motions/hachiware/running.gif" width="72" alt="ハチワレ 作業"></td><td><img src="assets/motions/hachiware/review.gif" width="72" alt="ハチワレ レビュー"></td><td><img src="assets/motions/hachiware/look.gif" width="72" alt="ハチワレ 16方向"></td></tr>
<tr><th><sub>うさぎ</sub></th><td><img src="assets/motions/usagi/idle.gif" width="72" alt="うさぎ 待機"></td><td><img src="assets/motions/usagi/running-right.gif" width="72" alt="うさぎ 走る →"></td><td><img src="assets/motions/usagi/running-left.gif" width="72" alt="うさぎ 走る ←"></td><td><img src="assets/motions/usagi/waving.gif" width="72" alt="うさぎ あいさつ"></td><td><img src="assets/motions/usagi/jumping.gif" width="72" alt="うさぎ ジャンプ"></td><td><img src="assets/motions/usagi/failed.gif" width="72" alt="うさぎ 失敗"></td><td><img src="assets/motions/usagi/waiting.gif" width="72" alt="うさぎ 待つ"></td><td><img src="assets/motions/usagi/running.gif" width="72" alt="うさぎ 作業"></td><td><img src="assets/motions/usagi/review.gif" width="72" alt="うさぎ レビュー"></td><td><img src="assets/motions/usagi/look.gif" width="72" alt="うさぎ 16方向"></td></tr>
<tr><th><sub>モモンガ</sub></th><td><img src="assets/motions/momonga/idle.gif" width="72" alt="モモンガ 待機"></td><td><img src="assets/motions/momonga/running-right.gif" width="72" alt="モモンガ 走る →"></td><td><img src="assets/motions/momonga/running-left.gif" width="72" alt="モモンガ 走る ←"></td><td><img src="assets/motions/momonga/waving.gif" width="72" alt="モモンガ あいさつ"></td><td><img src="assets/motions/momonga/jumping.gif" width="72" alt="モモンガ ジャンプ"></td><td><img src="assets/motions/momonga/failed.gif" width="72" alt="モモンガ 失敗"></td><td><img src="assets/motions/momonga/waiting.gif" width="72" alt="モモンガ 待つ"></td><td><img src="assets/motions/momonga/running.gif" width="72" alt="モモンガ 作業"></td><td><img src="assets/motions/momonga/review.gif" width="72" alt="モモンガ レビュー"></td><td><img src="assets/motions/momonga/look.gif" width="72" alt="モモンガ 16方向"></td></tr>
<tr><th><sub>シーサー</sub></th><td><img src="assets/motions/shisa/idle.gif" width="72" alt="シーサー 待機"></td><td><img src="assets/motions/shisa/running-right.gif" width="72" alt="シーサー 走る →"></td><td><img src="assets/motions/shisa/running-left.gif" width="72" alt="シーサー 走る ←"></td><td><img src="assets/motions/shisa/waving.gif" width="72" alt="シーサー あいさつ"></td><td><img src="assets/motions/shisa/jumping.gif" width="72" alt="シーサー ジャンプ"></td><td><img src="assets/motions/shisa/failed.gif" width="72" alt="シーサー 失敗"></td><td><img src="assets/motions/shisa/waiting.gif" width="72" alt="シーサー 待つ"></td><td><img src="assets/motions/shisa/running.gif" width="72" alt="シーサー 作業"></td><td><img src="assets/motions/shisa/review.gif" width="72" alt="シーサー レビュー"></td><td><img src="assets/motions/shisa/look.gif" width="72" alt="シーサー 16方向"></td></tr>
<tr><th><sub>ラッコ</sub></th><td><img src="assets/motions/rakko/idle.gif" width="72" alt="ラッコ 待機"></td><td><img src="assets/motions/rakko/running-right.gif" width="72" alt="ラッコ 走る →"></td><td><img src="assets/motions/rakko/running-left.gif" width="72" alt="ラッコ 走る ←"></td><td><img src="assets/motions/rakko/waving.gif" width="72" alt="ラッコ あいさつ"></td><td><img src="assets/motions/rakko/jumping.gif" width="72" alt="ラッコ ジャンプ"></td><td><img src="assets/motions/rakko/failed.gif" width="72" alt="ラッコ 失敗"></td><td><img src="assets/motions/rakko/waiting.gif" width="72" alt="ラッコ 待つ"></td><td><img src="assets/motions/rakko/running.gif" width="72" alt="ラッコ 作業"></td><td><img src="assets/motions/rakko/review.gif" width="72" alt="ラッコ レビュー"></td><td><img src="assets/motions/rakko/look.gif" width="72" alt="ラッコ 16方向"></td></tr>
<tr><th><sub>くりまんじゅう</sub></th><td><img src="assets/motions/kurimanju/idle.gif" width="72" alt="くりまんじゅう 待機"></td><td><img src="assets/motions/kurimanju/running-right.gif" width="72" alt="くりまんじゅう 走る →"></td><td><img src="assets/motions/kurimanju/running-left.gif" width="72" alt="くりまんじゅう 走る ←"></td><td><img src="assets/motions/kurimanju/waving.gif" width="72" alt="くりまんじゅう あいさつ"></td><td><img src="assets/motions/kurimanju/jumping.gif" width="72" alt="くりまんじゅう ジャンプ"></td><td><img src="assets/motions/kurimanju/failed.gif" width="72" alt="くりまんじゅう 失敗"></td><td><img src="assets/motions/kurimanju/waiting.gif" width="72" alt="くりまんじゅう 待つ"></td><td><img src="assets/motions/kurimanju/running.gif" width="72" alt="くりまんじゅう 作業"></td><td><img src="assets/motions/kurimanju/review.gif" width="72" alt="くりまんじゅう レビュー"></td><td><img src="assets/motions/kurimanju/look.gif" width="72" alt="くりまんじゅう 16方向"></td></tr>
<tr><th><sub>セイレーン</sub></th><td><img src="assets/motions/siren/idle.gif" width="72" alt="セイレーン 待機"></td><td><img src="assets/motions/siren/running-right.gif" width="72" alt="セイレーン 走る →"></td><td><img src="assets/motions/siren/running-left.gif" width="72" alt="セイレーン 走る ←"></td><td><img src="assets/motions/siren/waving.gif" width="72" alt="セイレーン あいさつ"></td><td><img src="assets/motions/siren/jumping.gif" width="72" alt="セイレーン ジャンプ"></td><td><img src="assets/motions/siren/failed.gif" width="72" alt="セイレーン 失敗"></td><td><img src="assets/motions/siren/waiting.gif" width="72" alt="セイレーン 待つ"></td><td><img src="assets/motions/siren/running.gif" width="72" alt="セイレーン 作業"></td><td><img src="assets/motions/siren/review.gif" width="72" alt="セイレーン レビュー"></td><td><img src="assets/motions/siren/look.gif" width="72" alt="セイレーン 16方向"></td></tr>
<tr><th><sub>古本屋</sub></th><td><img src="assets/motions/furuhonya/idle.gif" width="72" alt="古本屋 待機"></td><td><img src="assets/motions/furuhonya/running-right.gif" width="72" alt="古本屋 走る →"></td><td><img src="assets/motions/furuhonya/running-left.gif" width="72" alt="古本屋 走る ←"></td><td><img src="assets/motions/furuhonya/waving.gif" width="72" alt="古本屋 あいさつ"></td><td><img src="assets/motions/furuhonya/jumping.gif" width="72" alt="古本屋 ジャンプ"></td><td><img src="assets/motions/furuhonya/failed.gif" width="72" alt="古本屋 失敗"></td><td><img src="assets/motions/furuhonya/waiting.gif" width="72" alt="古本屋 待つ"></td><td><img src="assets/motions/furuhonya/running.gif" width="72" alt="古本屋 作業"></td><td><img src="assets/motions/furuhonya/review.gif" width="72" alt="古本屋 レビュー"></td><td><img src="assets/motions/furuhonya/look.gif" width="72" alt="古本屋 16方向"></td></tr>
<tr><th><sub>あのこ</sub></th><td><img src="assets/motions/anoko/idle.gif" width="72" alt="あのこ 待機"></td><td><img src="assets/motions/anoko/running-right.gif" width="72" alt="あのこ 走る →"></td><td><img src="assets/motions/anoko/running-left.gif" width="72" alt="あのこ 走る ←"></td><td><img src="assets/motions/anoko/waving.gif" width="72" alt="あのこ あいさつ"></td><td><img src="assets/motions/anoko/jumping.gif" width="72" alt="あのこ ジャンプ"></td><td><img src="assets/motions/anoko/failed.gif" width="72" alt="あのこ 失敗"></td><td><img src="assets/motions/anoko/waiting.gif" width="72" alt="あのこ 待つ"></td><td><img src="assets/motions/anoko/running.gif" width="72" alt="あのこ 作業"></td><td><img src="assets/motions/anoko/review.gif" width="72" alt="あのこ レビュー"></td><td><img src="assets/motions/anoko/look.gif" width="72" alt="あのこ 16方向"></td></tr>
<tr><th><sub>でかつよ</sub></th><td><img src="assets/motions/dekatsuyo/idle.gif" width="72" alt="でかつよ 待機"></td><td><img src="assets/motions/dekatsuyo/running-right.gif" width="72" alt="でかつよ 走る →"></td><td><img src="assets/motions/dekatsuyo/running-left.gif" width="72" alt="でかつよ 走る ←"></td><td><img src="assets/motions/dekatsuyo/waving.gif" width="72" alt="でかつよ あいさつ"></td><td><img src="assets/motions/dekatsuyo/jumping.gif" width="72" alt="でかつよ ジャンプ"></td><td><img src="assets/motions/dekatsuyo/failed.gif" width="72" alt="でかつよ 失敗"></td><td><img src="assets/motions/dekatsuyo/waiting.gif" width="72" alt="でかつよ 待つ"></td><td><img src="assets/motions/dekatsuyo/running.gif" width="72" alt="でかつよ 作業"></td><td><img src="assets/motions/dekatsuyo/review.gif" width="72" alt="でかつよ レビュー"></td><td><img src="assets/motions/dekatsuyo/look.gif" width="72" alt="でかつよ 16方向"></td></tr>
</table>

> Codexの状態名 `running` は作業中という意味なので、ここでは **作業** モーションです。画面を走るモーションは `running-right` と `running-left` です。

<details>
<summary>スプライト仕様</summary>

| 行 | 状態 | フレーム |
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
| 9 – 10 | 視線16方向（12時から時計回り） | 16 |

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

## ご注意

このリポジトリは非公式のファンメイドです。ちいかわのキャラクターと名称の権利は、原作者ナガノ氏および各権利者に帰属します。商用利用や再配布は許可していません。権利者からのご要望があれば、すぐに取り下げます。
