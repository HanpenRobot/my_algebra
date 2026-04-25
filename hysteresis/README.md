# 非線形微分方程式でカタストロフィとヒステリシスが発生する理由の説明


以下の実数パラメータ$`A , B`$をもつ1変数$`x`$に関する非線形微分方程式を考える。
```math
\frac{d x}{d t} = F(x,A,B)=-x^3 + Ax - B \cdots (1)
```
このとき、
```math
\frac{d x}{d t} = F(x,A,B)=-x^3 + Ax - B=0 \cdots (2)
```
を満たす$`x(t)=Const`$を微分方程式$`(1)`$の平衡点(不動点と呼ぶこともある)とよぶ。平衡点を$`x_e`$と表記する。
(平衡点はequilibrium pointなので、$`x_e`$という表記を採用した。)


さて、微分方程式$`(1)`$の平衡点$`x_e`$は$`-x^3 + Ax - B=0`$という３次方程式の実数解である。
この実数解の個数は$`A, B`$の値によって変わる。
> [!IMPORTANT]
> この個数は
> $`(1)`$と$`(3)`$の交点数=1になる$`A, B`$の値のときは、実数解の個数=1
> $`(1)`$と$`(3)`$の交点数=2になる$`A, B`$の値のときは、実数解の個数=3
>

```math
y=-x^3 + Ax \cdots (1) \\
y=B \cdots (2)
```
実数解の個数の変化について以下で説明する。
まず$`A<0`$のときの$`y=-x^3 + Ax`$のグラフの例を以下に示す。

![./cusp_anim001.gif](./cusp_anim001.gif)
*Fig.1 $`y=-x^3 -2x`$のプロット ($`x`$に関して単調現象なグラフなので任意の実数$`B`$に対して$`y=B`$と唯一の解をもつ$)*

![./cusp_anim002.gif](./cusp_anim002.gif)
*Fig.2 $`y=-x^3`$のプロット ($`x`$に関して単調現象なグラフなので任意の実数$`B`$に対して$`y=B`$と唯一の解をもつ$)*

![./cusp_anim006.gif](./cusp_anim006.gif)
*Fig.2 $`y=-x^3+3x`$のプロット ($`y=-x^3+3x`$のグラフには極大値と極小値が存在している。に$`y=B`$と唯一の解をもつ$)*


この実数解の個数は$`A, B`$の値によって異なる3個の解の場合と1個の解のときがある。これは以下のアニメーションを見ると理解できる。

![./cusp_anim.gif](./cusp_anim.gif)
*Fig.1 $`y=-x^3 + Ax`$と$`y=B`$の交点のプロット*




```math
-x^3 + Ax - B=0 \cdots (3) \\
-3x^2 + A =0 \cdots (4) \\
A=3x^2 \cdots (5) \\
```

$`(5)`$を$`(3)`$に代入すると

```math
-x^3 + Ax - B = -x^3 + (3x^2)x - B = 2x^3 - B = 0 \cdot (6) \\

\therefore \left( A,B \right) = (3x^2, 2x^3),  \left( -\infty <  x < \infty \right) \cdots (7)


```

<!-- \therefore \left( A,B \right) = (3x^2, 2x^3),  \left( x \in \mathbb{R} \right) \cdots (7) -->

<!-- ```math
-x^3 + Ax - B=0 \cdots (3) \\
-3x^2 + A =0 \cdots (4) \\
A=3x^2 \cdots (5) \\

(5)を(3)に代入すると
-x^3 + Ax - B = -x^3 + (3x^2)*x - B = -x^3 ^ 3x^3 - B = 2x^3 = B \cdots (6) \\

\therefore \left( A,B \right) = (3x^2, 2x^3),  \left( x \in \mathbb{R} \right) \cdots (7)

``` -->
$`(7)`$の曲線はカスプ(cusp)と呼ばれる。$`(7)`$の曲線は以下である。

![./draw_cusp.gif](./draw_cusp.gif)
<!-- *Fig.1 カスプ\left( A,B \right) = (3x^2, 2x^3),  \left( x \in \mathbb{R} \right)のプロット* -->

$`-30 \le A,B \le 30`$の範囲で３次方程式$`-x^3 + Ax - B=0`$の実数解をもとめて3Dプロットしたものが以下の図である。

![./cubic_root_output1.gif](./cubic_root_output1.gif)
*Fig.1 ３次方程式$`-x^3 + Ax - B=0`$の実数解の3Dプロット(その1)*
![./cubic_root_output2.gif](./cubic_root_output2.gif)
*Fig.2 ３次方程式$`-x^3 + Ax - B=0`$の実数解の3Dプロット(その2)*


$`(1)`$を$`x`$で偏微分した結果は以下のようになる。

```math
\frac{\partial^2 x}{\partial x\partial t}(x) = \frac{d F}{d x}(x)=-3x^2 + A \cdots (3)
```
$`(3)`$を$`f(x)`$とおく。

このとき、$`\lvert x(t) - x_e \rvert \simeq 0`$のとき$`(1)`$に関して以下が成立する。
```math
\frac{d x}{d t} = f(x_e)(x-x_e) \cdots (4)
```
これは微分方程式$`(1)`$を平衡点$`x_e`$の近傍で線形近似した結果である。
このため、$`(4)`$の解は求めることが可能で
```math
x(t) = \exp \left( f(x_e)t \right) + x_e \cdots (5)
```
となる。

$`f(x_e)<0`$ならば、$`x_e`$は安定な平衡点と呼ぶ。<br>
$`f(x_e)>0`$ならば、$`x_e`$は不安定な平衡点と呼ぶ。<br>

![./slope_at_fixpoint.gif](./slope_at_fixpoint.gif)
*Fig.3 ３次方程式$`-x^3 + Ax - B=0`$の実数解$`x_e{(A,B)}=-3{x_e}^2 + A`$(平衡点)の3Dプロット(その1)*


![./slope_at_fixpoint2.gif](./slope_at_fixpoint2.gif)
*Fig.4 ３次方程式$`-x^3 + Ax - B=0`$の実数解$`x_e`$(平衡点)を$`\frac{d F}{d x}(x_e)=-3{x_e}^2 + A `$の3Dプロット(その2)*


$`x_e`$が安定な平衡点であるときに
微分方程式$`(1)`$を$`\lvert x(0) - x_e \rvert \simeq 0`$をみたす初期値$`x(0)`$でルンゲ・クッタ法などで変数$`t`$に関して数値積分すると
```math
\lim_{t\to\infty} x(t) = x_e
```
という結果になる。なぜならば$`f(x_e)<0`$なので
```math
\lim_{t\to\infty} \exp \left( f(x_e)t \right) = 0\cdots (6)
```
となるからである。もし$`x_e`$が不安定な平衡点であるときは初期値$`x(0)`$が$`x(0) \neq x_e`$である限りルンゲ・クッタ法などで変数$`t`$に関して数値積分すると
```math
\lim_{t\to\infty} x(t) = \infty\cdots (7)
```

という結果になる。なぜならば$`f(x_e)>0`$なので
```math
\lim_{t\to\infty} \exp \left( f(x_e)t \right) = \infty\cdots (8)
```






```math
-3x^2 + A = 0 \Leftrightarrow x = \pm \sqrt {\frac{A}{3}} \cdots (3)
```

```math
G(x)=-x^3 + Ax \cdots (4)
```
とするとき



$`(5)`$の不等式を満たす$`A , B`$で解の個数は3個になる。
```math
A > 0 \wedge \left| -\left(\sqrt{\frac{A}{3}}\right)^3 + A\sqrt{\frac{A}{3}} \right| < B \cdots (5)
```

$`(6)`$の不等式を満たす$`A, B`$で解の個数は1個になる。

```math
A \le 0 \vee \left| -\left(\sqrt{\frac{A}{3}}\right)^3 + A\sqrt{\frac{A}{3}} \right| \ge B \cdots (6)
```

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