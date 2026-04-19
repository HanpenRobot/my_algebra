import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sympy import Eq, solve, symbols

sns.set(style="darkgrid")


def cusp(x, a):
    return -x ^ 3 + a * x


L = 30
A = list(np.arange(-L, L, 1))
B = list(np.arange(-L, L, 1))

ans_A = []
ans_B = []
ans_Z = []

for a in A:
    for b in B:
        if a > 0.0:
            s = symbols("s")
            equ = Eq(-(s**3) + a * s + b, 0)
            solutions = solve(equ, s)
            solutions = [
                complex(x).real for x in solutions if np.abs(complex(x).imag) < 0.001
            ]
        else:
            solutions = [0]
        print(f"{a=}, {b=}, {solutions=}, {len(solutions)=}")
        for tmp_ans in solutions:
            ans_A.append(a)
            ans_B.append(b)
            ans_Z.append(tmp_ans)

# fig = plt.figure(figsize=(8, 6))
# ax = fig.add_subplot(111, projection="3d")
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
sc = ax.scatter(ans_A, ans_B, ans_Z, c=ans_Z, cmap="viridis", marker="o")
ax.set_xlabel("A")
ax.set_ylabel("B")
ax.set_zlabel("x")
plt.title("Seabornスタイルの3D散布図")

plt.colorbar(sc)
plt.show()


# -(s**3) + a * s + b = 0
# -3s^2 = -a
# s = np.sqrt(a/3)

#

# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np
# from mpl_toolkits.mplot3d import Axes3D

# # Seabornスタイルを適用
# sns.set(style="darkgrid")

# # データ生成
# x = np.random.rand(100)
# y = np.random.rand(100)
# z = x**2 + y**2

# # 3Dプロットの作成
# fig = plt.figure(figsize=(8, 6))
# ax = fig.add_subplot(111, projection="3d")
# sc = ax.scatter(x, y, z, c=z, cmap="viridis", marker="o")

# # 軸ラベルとタイトル
# ax.set_xlabel("X軸")
# ax.set_ylabel("Y軸")
# ax.set_zlabel("Z軸")
# plt.title("Seabornスタイルの3D散布図")

# plt.colorbar(sc)
# plt.show()
