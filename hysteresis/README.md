# 非線形微分方程式のヒステリシスとカタストロフィを平衡点解析とルンゲ・クッタ法で説明する。
# カスプとヒステリシスを表現する微分方程式についての解説


以下の実数パラメータ$`A , B`$をもつ1変数の微分方程式を考える。注意: $`-x^3 + Ax - B`$でないと以下の議論は正しくない $`x^3 + Ax - B`$では違う結果になる。
```math

\frac{d x}{d t} = F(x)=-x^3 + Ax - B \cdots (1)
```
このとき、
```math
\frac{d x}{d t} = F(x)=-x^3 + Ax - B=0 \cdots (2)

```
を満たす$`x(t)=Const`$を微分方程式$`(1)`$の平衡点とよぶ。平衡点を$`x_e`$とする。
(平衡点はequilibrium pointなので、$`x_e`$という記載を採用した。)

$`(1)`$を$`x`$で偏微分した結果を$`f(x)`$とする。

```math
f(x) = \frac{\partial^2 x}{\partial x\partial t} = \frac{d F}{d x}=-3x^2 + A
```

$`\lvert x(t) - x_e \rvert \simeq 0`$のとき$`(1)`$に関して以下が成立する。
```math
\frac{d x}{d t} = f(x_e)(x-x_e)
```
これは微分方程式$`(1)`$を平衡点$`x_e`$の近傍で線形近似した結果である。
このため、平衡点$`x_e`$の近傍で
```math
x(t) = \exp \Big( f(x_e)t \Big) + x_e
```
となる。

$`f(x_e)<0`$ならば、$`x_e`$は安定な平衡点と呼ぶ。<br>
$`f(x_e)>0`$ならば、$`x_e`$は不安定な平衡点と呼ぶ。<br>
$`x_e`$が安定な平衡点であるときに
微分方程式$`(1)`$を$`\lvert x(0) - x_e \rvert \simeq 0`$をみたす初期値$`x(0)`$でルンゲ・クッタ法などで変数$`t`$に関して数値積分すると
```math
\lim_{t\to\infty} x(t) = x_e
```
という結果になる。$`f(x_e)<0`$なので
```math
\lim_{t\to\infty} \exp \Big( f(x_e)t \Big) = 0
```
となることに注意。

さて、微分方程式$`(1)`$の平衡点$`x_e`$は$`x^3 + Ax - B=0`$という３次方程式の解である。
この解の個数は$`A, B`$の値によって異なる3個の解の場合と1個の解のときがある。解の個数は

```math
-3x^2 + A = 0 \Leftrightarrow x = \pm \sqrt {\frac{A}{3}} \cdots (3)
```

```math
G(x)=-x^3 + Ax \cdots (4)
```
とするとき


```math
G(\sqrt {\frac{A}{3}} )=-\Big(\sqrt{\frac{A}{3}}\Big)^3 + A\sqrt{\frac{A}{3}} \cdots (4)
```

```math
\therefore \left| -\Big(\sqrt{\frac{A}{3}}\Big)^3 + A\sqrt{\frac{A}{3}} \right| < B \cdots (5)
```
$`(5)`$の不等式を満たす$`A, B`$で解の個数は3個になる。

```math
\therefore \left| -\Big(\sqrt{\frac{A}{3}}\Big)^3 + A\sqrt{\frac{A}{3}} \right| \ge B \cdots (6)
```
$`(5)`$の不等式を満たす$`A, B`$で解の個数は1個になる。

<!--

まず、$`F(x)`$を$`x`$で微分したときに$`0`$になる点を求める。
```math
\frac{\partial^2 x}{\partial x\partial t} = \frac{d F}{d x}=-3x^2 + A =0
```
より
```math
\therefore x = \pm\frac{\sqrt{A}} {3}
```
となる。以下のアニメーションからわかるように$`A \neq 0`$であれば
```math
F(x)=-x^3 + Ax - B = 0
```
を満たす点 (つまり$`F(x)`$の零点)が3個出現することがわかる。
$`A = 0`$であれば$`F(x)`$の零点は$`x=0`$のみである。




ここで、
```math
\frac{d x}{d t} =F(x)= -x^3 + Ax - B = 0
```
を満たす変数$`t`$に関する定数関数$` x = h `$を求める。

つまり、
```math
\frac{\partial^2 x}{\partial x\partial t} = \frac{d F}{d x}=-3x^2 + A =0
```
```math
\therefore x = \pm\frac{\sqrt{A}} {3}
```


を満たす定数関数$`h(A,B)`$は微分方程式 $`(1)`$の不動点である。
不動点には安定性という概念が存在する。

ところで、$`F(x)=x^3 - Ax - B`$は3次関数なので$`\frac{d F}{d x}=0`$となる点$`x`$ (極大値 or 極小値)が不動点である。
ゆえに

```math
\frac{d F}{d x}=3x^2 - A =0
```
```math
\therefore x = \pm\frac{\sqrt{A}} {3}
```


```math
F(\frac{\sqrt{A}} {3})= {\frac{\sqrt{A}} {3}}^3 - A\frac{\sqrt{A}} {3} - B = 0

``` -->