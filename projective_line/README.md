# draw projective_line
![./projective_line_plot.gif](./projective_line_plot.gif)射影直線と`X=1`, `Y=1`の交点を表示する`gif`
> [!NOTE]
> 1次元射影直線$`RP^1`$の定義は以下である。
> ```math
> RP^1=原点を通る直線の集合
> ```
> つまり、$`RP^1`$は2次元平面$`R^2`$ (つまり、**2次元座標平面**)
> ```math
> R^2=\{(x_0,x_1) | x_0, x_1 \in R \}
> ```
> に以下の同値関係$`\sim`$
> ```math
> R^2 \setminus \{ 0 \} \ni (x_0,x_1) = \alpha (x_0',x_1') \iff (x_0,x_1) \sim (x_0',x_1')
> ```
> をいれた時の商集合
> ```math
> RP^1 = R^2 / \sim
> ```
> である。

> [!IMPORTANT]
> 1次元射影直線$`RP^1`$の要素は**座標**ではなく、**原点を通る直線**であることに注意 !
> ```math
> RP^1 \ni 原点を通る直線
> ```

> [!NOTE]
> 1次元直線$`R^1`$ (いわゆる、数直線)は1次元射影直線$`RP^1`$に以下のように写像$`f(x) := (x,1)`$を使って埋め込める。
> ```math
> f: R^1 \rightarrow RP^1
> ```
> ```math
> R^1 \ni x \mapsto f(x)=(x,1)=\left(  1,\frac{1}{x} \right) \in RP^1
> ```

> [!WARNING]
> $`RP^1 \ni \lim_{x \to \infty}\left(  1,\frac{1}{x} \right) = (1,0)`$に関数$`f`$で写像される$`R^1`$の要素は存在しない !
> ```math
> f: R^1 \simeq RP^1 \setminus {(1,0)}
> ```
