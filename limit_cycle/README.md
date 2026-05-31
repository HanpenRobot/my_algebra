# リミットサイクルをもつ微分方程式を4次のルンゲ・クッタ法で解いた結果

+ $`(1)`$,$`(2)`$で定義された連立微分方程式はリミットサイクルをもつ。
+ 微分方程式を解く際に使用したルンゲ・クッタ法のコードは[./runge_kutta_limit_cycle.c](./runge_kutta_limit_cycle.c)である。 (このコードは参考文献[2]のコードを参考に実装した)。

```math
\frac{dx}{dt}=a x- b y -x(x^2+y^2) \cdots (1)
```

```math
\frac{dy}{dt}=b x + a y -y (x^2+y^2) \cdots (2)
```

![./vec_field_ans_limit_cycle.gif](./vec_field_ans_limit_cycle.gif)
*Fig. 1 任意の初期値$`(x_0,y_0)`$から出発した解軌道が、$`t \to \infty`$で半径$`\sqrt{a}`$のリミットサイクルに収束していることが確認できる。また、$`(x,y)=(0,0)`$が不動点であることもわかる(しかし、$`(x,y)=(0,0)`$は不安定な不動点なので、わずかにでも0からずれるとリミットサイクルに収束する様子がアニメーションからも確認できる。)*

# リミットサイクルが発生する理由
```math
x(t)=r(t)\cos(\theta(t)) \cdots (3)
```
<!-- \left(\theta(t)\right) -->
```math
y(t)=r(t)\sin(\theta(t)) \cdots (4)
```

+ $`(3)`$,$`(4)`$の変数変換で、$`(1)`$,$`(2)`$を極座標$`0 \le r \le \infty, 0 \le \theta < 2\pi`$に関する微分方程式に変換する。
+ $`(3)`$,$`(4)`$から$`(5)`$が成立することに注意$`\left(\cos^2(\theta)+\sin^2(\theta)=1\right)`$。
```math
x^2+y^2=r(t)^2 \cdots (5)
```

## 極座標形式へ方程式を変換
```math
\frac{dx}{dt}=\frac{dr}{dt}\cos(\theta)-r(t)\sin(\theta) \frac{d\theta}{dt}=a r\cos(\theta) -b r\sin(\theta) - r^3\cos(\theta) \cdots (6)
```

```math
\frac{dy}{dt}=\frac{dr}{dt}\sin(\theta)+r(t)\cos(\theta) \frac{d\theta}{dt}=b r\cos(\theta) +a r\sin(\theta) - r^3\sin(\theta) \cdots (7)
```

+ $`(6)+(7)`$を計算すると
```math
\frac{dr}{dt}\left(\cos(\theta)+\sin(\theta)\right)+r\frac{d\theta}{dt}(\cos(\theta)-\sin(\theta))=r(a-r^2)\left(\cos(\theta)+\sin(\theta)\right)+br\left(\cos(\theta)-\sin(\theta)\right) \cdots (8)
```
+ $`\left(\cos(\theta)+\sin(\theta)\right)`$と$`\left(\cos(\theta)-\sin(\theta)\right)`$の項を比較すると
```math
\frac{dr}{dt}=r(a-r^2) \cdots (9)
```

```math
\frac{d\theta}{dt}=b \cdots (10)
```

- 参考文献[1] 新版 基礎からの力学系 分岐解析からカオス的遍歴へ サイエンス社 2005年 新版第1刷発行, pp. 88-89
- 参考文献[2] C言語による数値計算入門 第2版 新装版 堀之内 總一・酒井幸吉・榎園茂 森北出版株式会社 2015年 第2版装版第1刷発行, pp.128-129

