# 厳密計算の再現

2026-11-25 / v1.0

いずれも Python 3 の標準ライブラリのみを使用する。浮動小数点や外部サービスは不要。repoのルートで実行する。

```sh
python computations/schwarzenberger.py --verify
python computations/jet_defects.py --verify
```

## Schwarzenberger 条件

`schwarzenberger.py` は二つの独立な方法を比較する。Newton係数は形式Chern根の微分方程式から有理数漸化式で求め、最初の非p整数次数は判別式の素数別公式で求める。証明・先行研究比較は `notes/arithmetic_obstructions.md` にある。

既定の検算範囲は c1=−3,…,3、c2=−40,…,200 の1687組、係数次数48まで、15素数。P5/P6/P7の剰余類と例も再現する。この有限計算だけから一般定理や束の実在性を結論しない。

## 有限厚化の Jordan 欠損

`jet_defects.py` は A=Q[x0,x1,x2,x3]/(xi^d) の実際の単項式基底を使い、h=x0+…+x_(q−1) の冪乗法行列を構成する。階数は整数の分数なし消去法で厳密に計算する。行列計算側ではsl2分解を使用しない。

核の次元から制限余核の各次数を求め、原稿のJordan分解・Hilbert関数による予測と比較する。既定範囲はd=1,…,4、q=1,…,4、最初の欠損次数の次までで、40個の(d,q,k)と456個の乗法階数を確認する。単なる最初の非零だけでなく、対象のすべての次数の次元を比較する。

一般の証明は `papers/hartshorne.tex` を正本とし、形式証明器による検証は実施していない。大量の生成行列・キャッシュは保存しない。
