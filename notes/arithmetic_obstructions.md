# Schwarzenberger 条件の素数別延長限界

2026-11-25 / v1.0。現行研究ノート。

## 位置付け

以下は階数2束の存在を証明するものではなく、Chern 類が定める**整係数仮想 K 類**の完全な数値判定である。中央階乗積は Feder–Gitler の既知の式であり、奇素数の局所分類は Granja の既知の Feder–Gitler 局所分類の帰結に相当する。ここでの独立作業は、射影空間上の階数2 Schwarzenberger 条件へ翻訳し、最初に破れる次元を 2-primary 部分を含めて明示し、独立な有理数計算で検証したことである。新しい幾何学的分解定理・新規性の確定した論文成果として扱わない。

## 1. 整係数 K 類と Newton 係数

整数 c1,c2 に対し α+β=c1, αβ=c2 とする。x=[O(1)]−1 と置くと

  F(x)=(1+x)^α+(1+x)^β=Σ b_j x^j,
  b_j=binom(α,j)+binom(β,j).

K(P^n)=Z[x]/(x^{n+1}) なので b_0,…,b_n が整数であることが、この形式 Chern character を持つ整係数 K 類が存在するための必要十分条件である。これは全 twist の Euler characteristic の整数性（Schwarzenberger 条件）と同値。K の Euler pairing は unimodular であり、[O],…,[O(n)] は整係数基底なので「全 twist」から K の整数性へ戻せる。

微分方程式 ((1+x)∂x)^2F−c1((1+x)∂x)F+c2F=0 により

  b_0=2, b_1=c1,
  b_{j+2}=−[(j+1)(2j+1−c1)b_{j+1}+(j²−c1 j+c2)b_j]/[(j+2)(j+1)].

この漸化式は、下記の局所公式を使わない独立な厳密検算に使う。

整数 twist は F に (1+x)^a を掛ける操作なので、各素数 p について最初の非 p 整係数の次数を変えない。c1=0 または −1 に正規化できる。

### λ 演算による追加の RR 整数性は独立な障害にならない

F が整係数 K 類ならば

  λ_t(F)=1+F t+[O(c1)]t²

が K(P^n)[[t]] で成立する。証明は Q 係数 Chern character と Adams 演算で

  λ_t(F)=exp(Σ_{m≥1}(−1)^{m−1}ψ^m(F)t^m/m)
        =(1+e^{αH}t)(1+e^{βH}t)

と計算し、K(P^n) が torsion free であることを使う。従って任意の Schur 演算・tensor 演算・dual で得られる仮想類の全 twist の Euler characteristic も整数になる。これは実際の束による表現、正値性、コホモロジーの次元、幾何学的存在を意味しない。

## 2. 中央階乗積

y=x²/(1+x) と置く。D を任意の標数0係数体の元とすると

  (1+x)^{sqrt(D)}+(1+x)^{−sqrt(D)}
    =2+Σ_{j≥1} A_j(D)y^j,
  A_j(D)=2/(2j)! · Π_{i=0}^{j−1}(D−i²).

各 y^j は x^{2j} を先頭項とし、残りも整数係数を持つ。従って x^{n+1} を法とする整数性は、j≤floor(n/2) の A_j(D) の整数性と同値。

この式は Feder–Gitler (1973), Lemma 2.8（p.36）の式そのもの。自己完結な証明も簡単で、y^j の係数は D に関して次数 j、D=0,1²,…,(j−1)² で消え、D=j² で 1 になる。この最後の値は z^j+z^{−j} が y=z+z^{−1}−2 に関する monic j 次多項式になることから従う。

c1=0 の場合は D=−c2。c1=−1 の場合には別の展開

  F(x)=(2+x)/(1+x) · Σ_{j≥0} B_j(c2)y^j,
  B_0=1,
  B_j(c)= (−1)^j/(2j)! · Π_{i=0}^{j−1}(c+i(i+1))

が成立する。これは同様の補間か、cosh(δu/2)/cosh(u/2), δ²=1−4c, u=log(1+x) の微分方程式から得られる。

## 3. 奇素数で最初に破れる次元（完全判定）

Δ=c1²−4c2 とし、h_p を b_j が初めて Z_p に属さなくなる j、存在しないとき ∞ とする。p は奇素数。Δ=0 なら h_p=∞。Δ≠0 について s=v_p(Δ), u=p^{−s}Δ とすると

| Δ の局所型 | h_p |
| --- | --- |
| s=2a, u が mod p の平方 | ∞ |
| s=2a, u が mod p の非平方 | p^a(p+1) |
| s=2a+1 | 2p^{a+1} |

有限の場合、初めて失敗する係数の p 進付値はちょうど −1。

### 証明

(1+x)^{−c1/2} は Z_p[[x]] の単元なので、F を中心化し、D=Δ/4 の中央階乗積に移る。D の付値と単元平方型は Δ と同じ。平方の場合、sqrt(D)∈Z_p なので各二項係数が p 整である。

s=2a で単元が非平方の場合、i=0 も含め

  v_p(D−i²)=2 min(v_p(i),a),

ここで v_p(0)=∞。したがって分子の付値は

  V_j=2Σ_{k=1}^a ceil(j/p^k),

分母の付値は W_j=Σ_{k≥1}floor(2j/p^k)。q=p^a、j0=q(p+1)/2 とする。j<j0 のとき k>a の尾部は floor(2j/(pq))≤1 だけである。j が q の倍数でなければ k=a の

  2ceil(j/q)−floor(2j/q)

が少なくとも1なので V_j≥W_j。j が q の倍数なら j/q≤(p−1)/2 なので尾部は0。j=j0 では各 k≤a の差が0、尾部が1となり V_j−W_j=−1。a=0 でも同じ結論が直ちに成立する。

s=2a+1 の場合

  V_j=2Σ_{k=1}^a ceil(j/p^k)+ceil(j/p^{a+1}).

q=p^{a+1} とすると j<q では最後の ceil が1、対応する分母の尾部 floor(2j/q) は0または1なので非負。j=q で前半の差は0、最後が1−2=−1。p≥3 によりそれより高い分母項はない。これで最初の失敗を含めて証明された。

### 既知結果との比較

s=0 の場合の p+1 は、Ellia–Franco–Gruson の「p<n なら Δ は mod p で平方」という既知の障害を正確に再現する。全ての奇 p における局所解集合は、Granja, arXiv:math/0305315v3, Proposition 2.1 と式(2)（p.3）の Feder–Gitler 合同条件と同じ。そこでは quaternionic 次元 m を使うので、ここでは m=floor(n/2) と比較する。

## 4. p=2 の完全判定

まず整数 twist で c1=0 または −1 に正規化する。

### c1=−1

c2 が偶数なら Δ=1−4c2≡1 mod8。二根 (−1±sqrt(Δ))/2 は Z2 に属するので h2=∞。c2 が奇数なら b3=(3c2−2)/2 が半整数で、b0,b1,b2 は整数なので h2=3。

### c1=0

D=−c2。D=0 なら h2=∞。D≠0 について s=v2(D), u=2^{−s}D は奇数とする。

| D の局所型 | h2 |
| --- | --- |
| s=2a, u≡1 mod8 | ∞ |
| s=2a, u≡3,7 mod8 | 2^{a+2} |
| s=2a, u≡5 mod8 | 3·2^{a+1} |
| s=2a+1 | 2^{a+2} |

有限の場合、初めて失敗する係数の2進付値は −1。

### 証明

中央階乗係数 A_j(D) の付値は 1+V_j−W_j である。

s=2a+1 のとき V_j は奇 p の式で p=2 としたものと等しい。q=2^{a+1} とする。j<q では 1+V_j−W_j≥0。j=q では、分母の高次項が floor(2q/q)+floor(2q/(2q))=3、分子の最後の項が1なので値は −1。

s=2a、u≡3,5,7 mod8 のとき、q=2^a, h=v2(u−1)∈{1,2} と置く。奇数 t に対し v2(u−t²)=h なので

  V_j=2Σ_{k=1}^a ceil(j/2^k)
      +h(ceil(j/q)−ceil(j/(2q))).

h=1 の場合 j<2q で 1+V_j−W_j≥0、j=2q で −1。h=2 の場合 j≤2q では非負で j=2q で0、2q<j<3q では k=a の非零剰余項が不足を埋め、j=3q で −1。a=0 の境界も直接同じ式から従う。u≡1 mod8 なら D は Z2 の平方であり、整数性が全次数で成り立つ。

Feder–Gitler の quaternionic 自己写像では偶数 j の係数に追加の偶数性を課すため、2-primary の条件はここでの複素 K(P^n) の条件より強い。従って Granja Proposition 2.1 の p=2 の式をそのまま流用してはいけない。

## 5. 帰結

### 5.1 全次数の整数性

全ての n で Schwarzenberger 条件が成立するなら Δ は非負の整数平方である。これは上の局所分類から初等的に従う。Δ の奇素数付値が奇数なら有限の障害がある。奇素数付値が全て偶数の場合、非平方である可能性は2進付値・符号によるものだが、それらは p=2 の分類で検出される。Δ が非負平方なら c1 と sqrt(Δ) の偶奇が一致するため、二根は整数になる。

これは Chern データの数値的分解であって、個々の束の分解や Babylonian tower theorem の代用ではない。

### 5.2 奇数次元の冗長性

c1=0 では全ての m≥1 に対し、P^{2m} と P^{2m+1} の条件は同値。c1=−1 では P²→P³ に c2 の偶数性が追加されるが、それ以降は P^{2m} と P^{2m+1} が同値 (m≥2)。理由は奇素数の失敗次数が常に偶数で、2-primary の失敗は c1=−1 の n=3 だけだからである。

### 5.3 有限段階には負の判別式の解が無限にある

任意の固定 n に対して、c1=0 または −1 の各場合で、c2 の正の等差数列全体が条件を満たす。粗い十分条件は n!|c2。より鋭い「全ての整数 t に対して (c1,Mt) が n 次元で許容される最小 M」は以下。

* c1=−1, n≥3: M=2 Π_{3≤p<n, p prime} p。
* c1=0: 各奇素数 p に対する指数 e_p は、上の最小可能失敗次数（s=2a なら p^a(p+1)、s=2a+1 なら2p^{a+1}）が n を初めて超える s。2 の指数は、2^{a+2}>n を満たす最小 a≥0 の2倍。n≤3 では M=1。

必要性は素数ごとに単元非平方を持つ倍数を選べること、十分性は失敗次数の単調性から従う。c1=−1 では p|M が Δ≡1 mod p を保証し、逆に p∤M なら t を動かして Δ を非平方 mod p にできる。

| n | c1=0 の M | c1=−1 の M |
| --- | --- | --- |
| 5 | 12 | 6 |
| 6,7 | 180 | 30 |
| 8,9 | 5040 | 210 |
| 10,11 | 25200 | 210 |
| 12,13 | 831600 | 2310 |

M は全解集合の最小周期とは異なる。有限段階の λ 演算・Schur 演算の RR 整数性だけでは、負の判別式を一括排除できないことが具体的に分かる。この非排除そのものは、Benoist–Voisin の有限 CW 複体上の位相的束の構成より弱く、新規性を主張しない。

## 6. P5, P6, P7 の全解

P5:

* c1=0: c2≡0,3,8,11 mod12。
* c1=−1: c2≡0,4 mod6。

P6 と P7 は同じ:

* c1=0: c2 mod8∈{0,4,7}, c2 mod9∈{0,2,5,8}, c2 mod5∈{0,1,4}。周期360内に36類。
* c1=−1: c2≡0 mod2, c2 mod9∈{0,3,6,7}, c2 mod5∈{0,3,4}。周期90内に12類。

例: (c1,c2)=(0,20) は P7 まで全数値条件を通るが P8 で2-primary 障害が生じる。(−1,30) は P11 まで通るが P12 で p=11 の障害が生じる。いずれも実在する束を構成したという意味ではない。

## 7. 再現

`python computations/schwarzenberger.py --verify` は標準 Python の整数・Fraction だけを用いる。c1=−3,…,3、c2=−40,…,200 の1687組について、n=48までの微分方程式による Newton 係数と、15素数における局所高さ公式を照合した。全て一致した。上の表と例も同じ実行で再現できる。

証明の正しさは上の数学的議論による。有限計算は定理の証明でも形式証明器による検証でもない。

## 8. 一次資料と注意点

1. S. Feder and S. Gitler, *Mappings of quaternionic projective spaces*, Bol. Soc. Mat. Mexicana 18 (1973), 33–37. Lemma 2.8 (p.36) が中央階乗積、Theorem 1.1 と §3 が KSp に由来する追加の偶数性。原典: https://www.boletin.math.org.mx/pdf/2/18/BSMM(2).18.33-37.pdf 。
2. Gustavo Granja, *Self maps of HP^n via the unstable Adams spectral sequence*, arXiv:math/0305315v3. Proposition 2.1 と式(2), p.3。奇素数の局所解集合を既に記述している。原典: https://arxiv.org/pdf/math/0305315 。arXiv の版日は2014-06-20、PDF内部の日付は2018-11-06と相違するため、書誌では v3 を識別子にする。
3. Jan Samsonowicz, *Chern classes of bundles of rank two on P5*, Demonstratio Mathematica 26 (1993), 529–534, DOI 10.1515/dema-1993-0224。Theorem 2.1 (p.531) の c1=0 の類リストには欠落がある。
4. 同, *A remark to the “Chern classes of bundles of rank two on P5”*, Demonstratio Mathematica 27 (1994), DOI 10.1515/dema-1994-0232。Theorem 1 は欠落した residues 3,8,11 mod12 を補う。原典: https://www.degruyterbrill.com/document/doi/10.1515/dema-1994-0232/pdf 。なお correction に続く reducibility の文も修正前の形を残しており、c2=−1 の split bundle を考えるだけで、文字通り全ての residue に適用できないことが分かる。必要なのは訂正された congruence 部分だけである。
5. Ph. Ellia, D. Franco, L. Gruson, *Smooth divisors of projective hypersurfaces*, Comment. Math. Helv. 83 (2008), 原典: https://content.ems.press/assets/public/full-texts/serials/cmh/83/2/1654/online/10.4171-cmh-128.pdf 。慣性素数による判別式の障害は既知。§3 末尾、pp.383–384 の Claim とその証明を確認。

## 次の有益な接続

算術単独での非存在証明には既知の限界がある。数値的に許される最小 Chern データを選別してから、cohomology/monad の実現可能性、Serre 対応、実際の有限段階延長障害に接続する。数値的 extension height と、特定の束の geometric extension height を混同しない。
