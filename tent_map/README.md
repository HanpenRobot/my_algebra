# テント写像のリターンマップ

![./return_tent_map_init_0.2_alpha1.5.gif](./return_tent_map_init_0.2_alpha1.5.gif)
*Fig. 1 カオスになる場合*

![./return_tent_map_init_0.3.gif](./return_tent_map_init_0.3.gif)
*Fig. 2 周期解になる場合*

![./return_tent_map_init_0.2_alpha0.4.gif](./return_tent_map_init_0.2_alpha0.4.gif)
*Fig. 3 収束する場合*

## 区分線形の対称型テント写像の不変分布
+ テント写像$`x_{n+1}=T(x_n)`$の不変分布$`\rho(x)`$が一様分布になることを数値計算で示す。$`\rho(x)`$はテント写像$`(1)`$のヒストグラムを正規化することで求めた。

```math
x_{n+1}=T(x_n) =
\begin{cases}
  2x & (0 \le x < \frac{1}{2}) \\
  2(1-x)   & (\frac{1}{2} \le x \le 1)
\end{cases}\cdots (1)
```



![./tent_invariant_dist.png](./tent_invariant_dist.png)

*Fig. 4 テント写像の不変分布の数値計算結果, 分布はほぼ一様分布になっている*

- 参考文献 力学系入門 原著第3版 微分方程式からカオスまで Morris W.Hirsch , Stephen Smale , Robert L.Devaney , 桐木 紳 訳, 三波 篤郎 訳, 谷川 清隆 訳, 辻井 正人 訳 共立出版 2017年 原著第3版第1刷, p. 349
- 参考文献 改定増補 カオス力学の基礎 早間 慧 現代数学社 2002年 改訂第2版, p. 5, pp. 21-22

