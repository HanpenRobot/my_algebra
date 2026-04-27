# Lorentz方程式を4次のルンゲ・クッタ法で解いた結果の3Dプロット
+ 下記のLorentz方程式を$`\sigma = 10, R = 28, b = \frac{8}{3}`$、初期値$`x(0)=0.3, y(0)=0, z(0)=0`$の条件で4次のルンゲ・クッタ法で解き、その結果を3Dプロットした。ルンゲ・クッタ法のコードは[./runge_kutta_3d.c](./runge_kutta_3d.c) (参考文献[1]のコードを参考に実装した)。
```math
\frac{d x}{d t} = -\sigma x + \sigma y \cdots (1)
```
```math
\frac{d y}{d t} = R x - y - xz\cdots (2)
```
```math
\frac{d z}{d t} = - b z + x y \cdots (3)
```


![./lorentz_plot.gif](./lorentz_plot.gif)

![./lorentz_plot_anim.gif](./lorentz_plot_anim.gif)

- 参考文献[1] C言語による数値計算入門 第2版 新装版 堀之内 總一・酒井幸吉・榎園茂 森北出版株式会社 2015年 第2版装版第1刷発行, pp.128-129
- 参考文献[2] 解くための微分方程式と力学系理論 千葉逸人 現代数学社 2021年 初版第2刷発行, p.120
