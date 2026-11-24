# Hartshorne 分解予想と有限厚化の障害

2026-11-25 / v1.0

**再開時は [現行研究方針](00_research_plan.md) を最初に読む。** 正本はこのリポジトリの `main`。[research-hub](https://github.com/uedakazushi/research-hub) が研究全体の入口である。

標数0の P^n（n≥7）上の階数2ベクトル束の分解予想を最上位目標とする。完全交叉、P5/P6、有限延長、cohomology・syzygy・数値条件、関連する独立した問題を並行して扱う。

## 現在の成果と限界

**Hartshorne 予想自体は未解決。新しい次元範囲の分解定理は得ていない。** 現在は有限厚化の還元写像の余核を Jordan block から計算する一般公式と、正確な反例・検出例を原稿にした。証明と新規性は別に扱い、主原稿は新規性確認前の研究草稿である。

- **欠損公式：** H_k=(h^{k+1}=0) から H=(h=0) への H^{i−1} の制限余核は、H^i_*(F) の h-Jordan block のうち長さ≤kのものを、終端の次数付きで数える。有限次数の分解判定と regularity による上界が従う。
- **鋭い例：** P3 上の null-correlation 束の座標 d乗写像による引き戻しは rank2、c1=0、c2=d²。座標超平面では還元が d−1次まで分裂し、d次で初めて非分裂になる。最初の H0 欠損の総次元は d³。
- **超平面依存：** 同じ束の一般超平面では一次ですでに欠損 d が twist d−1 に現れる。一次式の台の大きさごとに最初のコホモロジー欠損を計算した。欠損零と層の分裂は同一視しない。
- **算術の再現基盤：** Schwarzenberger 条件の素数別の最初の失敗次数、P5/P6/P7 の全数値解、有限次元での無限の数値的候補を厳密に記述した。中央階乗積・奇素数分類は既知文献と比較し、実在する束の構成とは区別する。
- **本質的な障害：** 任意の束は線形射影によってすべての形式近傍へ延長する。問題は大域的な局所自由延長や、その実際の厚化構造にある。数値・位相条件だけで負の判別式を一括排除する方針にも既知の限界がある。

## 現行資料

| 資料 | 役割 |
| --- | --- |
| [00_research_plan.md](00_research_plan.md) | 目標、状態、優先順位、次の具体的な問題、一般原則・保存許可 |
| [AGENTS.md](AGENTS.md) | 研究・保存・検証・hub更新の実行指示 |
| [notes/research_notes.md](notes/research_notes.md) | 現在の数学的知識、未解決の接続、再開先 |
| [notes/arithmetic_obstructions.md](notes/arithmetic_obstructions.md) | 算術条件の証明、全剰余類、先行研究比較 |
| [notes/literature.md](notes/literature.md) | 一次文献の具体的な参照箇所、適用条件、確認範囲 |
| [papers/hartshorne.tex](papers/hartshorne.tex) | 主原稿「射影空間上のベクトル束の有限厚化とコホモロジーのJordan型」 |
| [computations/](computations/) | 厳密計算と再現手順 |

## 再現・組版

```sh
python computations/schwarzenberger.py --verify
latexmk
```

算術コードは Python 3 の標準ライブラリのみを使う。組版には LuaLaTeX、LuaTeX-ja、latexmk、BibTeX が必要。repo全体を VS Code で開き、LaTeX Workshop の既定レシピで組版する。PDFとSyncTeXは `build/`。PDF・中間生成物は追跡しない。

## 検証

- 欠損公式、次数のずれ、regularity境界、monadの局所自由性、座標超平面の実際の分裂、台ごとのJordan型を独立に論理点検した。
- 算術は1687組・係数次数48・15素数で Newton 係数の有理数漸化式と素数別高さ公式が一致。Jordan欠損は40例・456個の有理数体上の行列階数で全対象次数が一致。有限計算は一般証明・形式証明とは区別する。
- `latexmk` を実行したが、この実行環境には `lualatex.fmt` と LuaTeX-ja がなく、本文の組版開始前に停止した。PDF/SyncTeX生成・表示検査は未完了。LuaTeX-jaを含む完全なTeX Live/MacTeX環境での組版が必要。VS Code設定を移植したが、UI操作・形式証明器は未実行。

次の優先課題は、cohomology欠損が零の具体例で実際の延長類を計算し、有限厚化の公式を高次元rank2の幾何学的制約へ接続することである。詳細は研究方針を参照。
