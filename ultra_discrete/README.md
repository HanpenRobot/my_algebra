# 保存量を持つ微分方程式を4次のルンゲ・クッタ法でシュミレーションした結果: WIP

<!-- + Sliding mode制御のシステムを$`(1)`$, $`(2)`$, $`(3)`$に示す。 -->
+ 微分方程式を解く際に使用したルンゲ・クッタ法のコードは[./runge_kutta_4d.c](./runge_kutta_4d.c)である。 (このコードは参考文献[2]のコードを参考に実装した)。

<!-- ```math
\frac{dx}{dt}=y \cdots (1)
```

```math
\frac{dy}{dt}2y-x+u(x,y) \cdots (2)
```

```math
u(x,y)=-\varphi(x,y) \cdots (3)
```

```math
\varphi(x,y) \cdots (4)
``` -->

```math
\ddot{Q}_{1}=-Q_{1}(Q^2_1+\epsilon Q^2_2)
```
```math
\ddot{Q}_{2}=-Q_{2}(Q^2_2+\epsilon Q^2_1)
```


```math
\dot{Q}_1=X
```
```math
\dot{X}=-Q_{1}(Q^2_1+\epsilon Q^2_2)
```

```math
\dot{Q}_2=Y
```
```math
\dot{Y}=-Q_{2}(Q^2_2+\epsilon Q^2_1)
```


```math
\dot{W}=X
```
```math
\dot{X}=-W(W^2+\epsilon Z^2)
```

```math
\dot{Z}=Y
```
```math
\dot{Y}=-Z(Z^2+\epsilon W^2)
```

![./plot_4dA.gif](./plot_4dA.gif)
<!-- *Fig. 1 任意の初期値$`(x_0,y_0)`$から出発した解軌道が、$`t \to \infty`$で半径$`\sqrt{a}`$のリミットサイクルに収束していることが確認できる。また、$`(x,y)=(0,0)`$が不動点であることもわかる(しかし、$`(x,y)=(0,0)`$は不安定な不動点なので、わずかにでも0からずれるとリミットサイクルに収束する様子がアニメーションからも確認できる。)* -->

![./plot_4d_poncareE1.gif](./plot_4d_poncareE1.gif)


![./plot_4d_poncareE5.gif](./plot_4d_poncareE5.gif)

*Fig. 2 ポアンカレプロット*

- 参考文献[1]  力学の解ける問題と解けない問題 岩波講座 物理の世界 吉田春夫 岩波書店 2005年 第1刷発行 , pp. 41-42
- 参考文献[2] C言語による数値計算入門 第2版 新装版 堀之内 總一・酒井幸吉・榎園茂 森北出版株式会社 2015年 第2版装版第1刷発行, pp.128-129

