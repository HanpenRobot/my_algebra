# Arnold方程式を4次のルンゲ・クッタ法で解いた結果の3Dプロット
+ 下記のArnold方程式を$`A=1.0, B=0.5,C=0.3`$、初期値$`x(0)=3.0, y(0)=0.0, z(0)=3.0`$の条件と$`x(0)=4.2, y(0)=0.0, z(0)=3.0`$で4次のルンゲ・クッタ法で解き、その結果を3Dプロットした(Arnold方程式のパラメータと初期値$は参考文献[1]の値を利用した)。

+ 微分方程式を解く際に使用したルンゲ・クッタ法のコードは[./runge_kutta_3d_arnold.c](./runge_kutta_3d_arnold.c)である。 (このコードは参考文献[2]のコードを参考に実装した)。
```math
\frac{d x}{d t} = A\sin(z)+C\cos(y) \cdots (1)
```
```math
\frac{d y}{d t} = B\sin(x)+A\cos(z) \cdots (2)
```
```math
\frac{d z}{d t} = C\sin(y)+B\cos(x) \cdots (3)
```


![./arnold_plot.gif](./arnold_plot.gif)
*Fig.1 初期値$`x(0)=3.0, y(0)=0.0, z(0)=3.0`$のArnold方程式の解 カオス状になっている。*

![./arnold_plot_anim.gif](./arnold_plot_anim.gif)
*Fig.2 初期値$`x(0)=3.0, y(0)=0.0, z(0)=3.0`$のArnold方程式の解のアニメーション カオス状になっている。*

![./arnold_plot2.gif](./arnold_plot2.gif)
*Fig.3 初期値$`x(0)=4.2, y(0)=0.0, z(0)=3.0`$のArnold方程式の解 トーラス状になっている。*

![./arnold_plot_anim2.gif](./arnold_plot_anim2.gif)
*Fig.4 初期値$`x(0)=4.2, y(0)=0.0, z(0)=3.0`$のArnold方程式の解のアニメーション トーラス状になっている。*

- 参考文献[1] 非線形力学 岡本久 岩波書店 1994年 p.30-31
- 参考文献[2] C言語による数値計算入門 第2版 新装版 堀之内 總一・酒井幸吉・榎園茂 森北出版株式会社 2015年 第2版装版第1刷発行, pp.128-129

