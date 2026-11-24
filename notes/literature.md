# 一次資料・適用範囲・新規性の確認

2026-11-25 / v1.0。以下は実際に確認した資料と、その限界である。分野全体の調査完了や新規性確定を意味しない。

## 原点と近年の状況

- **R. Hartshorne**, *Varieties of small codimension in projective space*, Bull. AMS 80 (1974), 1017–1032。原典のAMS PDFは今回403となり全文取得できていない。分解予想の定式化と完全交叉予想との関係は下記Benoist–Voisin §2.1でも確認した。原典の全議論を今回再検証したとはしない。
- **O. Benoist and C. Voisin**, *On the smoothability problem with rational coefficients*, Rend. Lincei Mat. Appl.36 (2025),393–408, DOI [10.4171/RLM/1076](https://doi.org/10.4171/RLM/1076)。[刊行版PDF](https://ems.press/content/serial-article-files/52561?nt=1)の§2.1–2.3、Proposition3.1、Remark3.3を確認。§2.3 p400は非安定rank2分解の古い証明に重大なギャップがあることを明記する。非安定の場合を解決済みとしない。Proposition3.1 p403は有限CW複体上で指定Chern類の共通倍を実現する位相的rank r束を与える。CP^nではc1=0,c2>0の位相的rank2束が存在するため、位相・整数性だけの一括排除を目指す方針には限界がある。論文の巻年は2025、PDF copyrightは2026である。

## 有限厚化・延長

- **I. Coandă and G. Trautmann**, *The splitting criterion of Kempf and the Babylonian tower theorem*, Comm.Algebra34(7) (2006),2485–2488, DOI [10.1080/00927870600650655](https://doi.org/10.1080/00927870600650655)。[著者原稿 math/0411636](https://arxiv.org/pdf/math/0411636)全文を確認。p1の主定理は m>Σ_(i>0) dim Ext1(E,E(−i)) のとき P^{n+m}への大域的延長から分解を導く。p1–2の補題は、**既に大域的に局所自由な束**の各厚化から超平面への還元がO_H加群として分裂することを仮定する。任意の束の形式延長の存在とは異なる。本稿の欠損公式は同じ二つの完全列の有限次数での比較であり、既知の無限次数判定を新成果として扱わない。
- **G. R. Kempf**, *A criterion for the splitting of a vector bundle*, Forum Math.2 (1990),477–480。書誌と定理の内容はCoandă–Trautmannの原稿で確認したが、Kempf原典全文は今回取得していない。直接の証明入力は確認済みのCoandă–Trautmann補題と通常のcohomologyである。
- **L. Bădescu**, *Infinitesimal extensions of rank two vector bundles on submanifolds of small codimension*, [arXiv:1412.4746](https://arxiv.org/pdf/1412.4746)。Theorem2.4、Proposition2.1、Theorem3.1の記述を確認。滑らかなX⊂P^NでdimX≥(N+3)/2≥4、rank2束の一次近傍への延長と、十分高いtwistの切断の零点の正規束列の分裂を関係付ける。非線形埋め込みであり、線形射影による自動延長の議論をそのまま適用できない。

## Cohomology・syzygy・monad

- **G. Horrocks**, *Vector bundles on the punctured spectrum of a local ring*, Proc.LMS(3)14 (1964),689–713, DOI [10.1112/plms/s3-14.4.689](https://doi.org/10.1112/plms/s3-14.4.689)。出版社の書誌を確認。全中間cohomologyの消滅による分解判定を使用し、その具体的使用はCoandă–Trautmann p2でも確認した。原典の全証明を今回読み直したとはしない。
- **E. G. Evans and P. Griffith**, *The syzygy problem*, Ann.Math.114 (1981),**323–333**, DOI [10.2307/1971296](https://annals.math.princeton.edu/1981/114-2/p04)。後続文献の323–353という頁表示は採用しない。原論文全文は未取得。著者による [1983年の別証明](https://assets.cambridge.org/97805212/71257/excerpt/9780521271257_excerpt.pdf)、*Commutative Algebra: Durham 1981*, LMS LNS72,2–11 のp8の定理を確認。体を含む局所環上の有限射影次元のk-syzygyでrank<kなら自由。束への適用はノートで導出した。著者自身の [Oberwolfach 21/1981報告](https://oda.mfo.de/bitstream/handle/mfo/1134/full-text.pdf?isAllowed=y&sequence=1) p7でもrank r<nの束への系を確認。
- **I. Coandă**, *Infinitely stably extendable vector bundles on projective spaces*, [arXiv:0907.4040](https://arxiv.org/pdf/0907.4040)。Theorem1 p2は内側cohomologyの全消滅、全項が直線束の和の三項monad、無限安定延長可能性を同値にする。Lemma2 pp2–3は超平面での消滅伝播。Theorem7 p6はH1の最小生成元数とH2による有限安定延長上界を与える。ノートの支持集合公式はその基本的制限列の帰結として扱う。
- **N. Mohan Kumar, C. Peterson, A. P. Rao**, *Monads on projective spaces*, Manuscripta Math.112 (2003),183–189, DOI10.1007/s00229-003-0389-x。内側cohomologyのない非分解束のrank≥n−1という入力はCoandă原稿での引用・適用を確認。KPR原典全証明は未取得。rank2、n≥4では全項が直線束の和の三項monadによる非分解束の構成は不可。一般のBeilinson複体や非分解中間項を排除する主張ではない。
- **F. Malaspina and A. P. Rao**, *Rank two bundles on P^n with isolated cohomology*, Bull.LMS55 (2023),2493–2504, DOI [10.1112/blms.12877](https://doi.org/10.1112/blms.12877)、[原稿](https://arxiv.org/pdf/2202.00304)。刊行版Theorem3.6はk>1、n≥4kの孤立型(n,k)を排除。Corollary3.5はn≥8かつH^i_*=0（3≤i≤n−3）なら分解。Proposition2.3はn≥6のrank2非分解束で一つでも内側cohomologyが消えると最小monadの中間項に直線束因子がないことを述べる。原稿版と刊行版の定理番号を混ぜない。
- **G. Fløystad**, *Monads on projective space*, [arXiv:math/9806147](https://arxiv.org/pdf/math/9806147)。主定理p1の線形複体の存在条件は左射の層としての単射と部分束としての単射を区別する必要がある。rank落ちの条件を確認せず高次元rank2束が得られると結論しない。

## 古典幾何・数値条件

- **P. Ellia, D. Franco, L. Gruson**, *Smooth divisors of projective hypersurfaces*, Comment.Math.Helv.83 (2008),371–385, DOI [10.4171/CMH.128](https://doi.org/10.4171/CMH.128)、[刊行版](https://content.ems.press/assets/public/full-texts/serials/cmh/83/2/1654/online/10.4171-cmh-128.pdf)。Theorem3.9はn≥5の滑らかな余次元2・subcanonicalな非完全交叉について、最小包含超曲面次数s≥n+1を与える。§3末尾 pp383–384の数論的Claimは、rank2束がP^n上に存在すれば任意の素数p<nについて判別式がmod pで平方（零を含む）であること。算術ノートのs=0の場合はこの既知条件である。
- Feder–Gitler、Granja、Samsonowiczとその訂正の正確な式・一次リンク・確認範囲は [算術ノート第8節](arithmetic_obstructions.md) を参照。特に原論文の誤った剰余類リストを使わない。

## 主原稿の新規性を確認する次の範囲

KempfとCoandă–Trautmannの有限段階の精密化、Lefschetz/Jordan型とcohomology module、冪引き戻しnull-correlationの既存研究を重点的に照合する。原稿に完全証明を書いたことや検索で一致する題名がなかったことを、新規性の証明としない。コホモロジー欠損と実際の延長類の差を示す具体例・幾何学的帰結を優先する。
