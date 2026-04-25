import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

CURVE_LINE_COLOR = "#0000FF"
RT_LINE_COLOR = "#FF0000"
XY_LINE_COLOR = "#00AA00"
X_AXIS_LINE_COLOR = "#000000"
Y_AXIS_LINE_COLOR = "#000000"
GRID_COLOR = "#444444"

LINE_WIDTH = 1
AXIS_LINE_WIDTH = 0.8
GRID_LINE_WIDTH = 0.8


FIGURE_SIZE = (10, 10)
AXIS_MAX = 10
AXIS_MIN = 0.0
TITLE_FONT_SIZE = 14
LABEL_FONT_SIZE = 20

FRAMES = 100
CONST_A = 3.2
INIT_VALUE = 0.63
fig = plt.figure(dpi=256)

plt.axes().set_aspect("equal")


def cusp(x: float, A: float) -> float:
    return -(x**3) + A * x


def draw(n: int):
    print(f"plotting {n=} ...")
    # A = [-2.0]
    A = list(np.arange(-5, 5, 0.1))
    plt.cla()
    plt.title(f"A=${A[n]:.2f}$", fontsize=TITLE_FONT_SIZE, loc="left")
    plt.xlabel(r"$x$", fontsize=LABEL_FONT_SIZE)
    plt.ylabel(r"$y$", fontsize=LABEL_FONT_SIZE)
    plt.grid(which="both", color=GRID_COLOR, linestyle="--", linewidth=GRID_LINE_WIDTH)

    plt.axhline(0, color=X_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.axvline(0, color=Y_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.xlim(-AXIS_MAX, AXIS_MAX)
    plt.ylim(-AXIS_MAX, AXIS_MAX)
    grid_list = np.arange(-AXIS_MAX, AXIS_MAX, 1.0)
    plt.xticks(grid_list)
    plt.yticks(grid_list)

    X = []
    Y = []
    L = 100
    start_value = -20.0
    step_value = 0.2
    print(f"{n=}, {A[n]=}")
    N = 300
    for x in range(N):
        X.append(start_value)
        Y.append(cusp(x=start_value, A=A[n]))
        x_h = np.sqrt(A[n] / 3.0)
        cusp_value = cusp(x=x_h, A=A[n])
        start_value += step_value
    plt.plot(
        X,
        Y,
        label=r"$y=-x^3+Ax$",
        color=RT_LINE_COLOR,
        linewidth=LINE_WIDTH,
    )
    if A[n] > 0:
        # plt.plot(
        #     [x_h, x_h],  # 縦棒
        #     [0, cusp_value],
        #     # label=f"y=B={cusp_value:.2f}",
        #     color="#000000",
        #     linewidth=LINE_WIDTH,
        #     linestyle="--",
        # )
        # plt.plot(
        #     [x_h, x_h],  # 極大値にマーカーを表示
        #     [0, cusp_value],
        #     # label=f"y=B={cusp_value:.2f}",
        #     "x",
        #     6,
        #     color="#000000",
        # )
        # plt.plot(
        #     [x_h],  # 極大値を取る時のx座標にマーカーを表示
        #     [0],
        #     "x",
        #     8,
        #     label=f"(x,y)=(0,{x_h:.2f})",
        #     color="#0000AA",
        # )
        plt.plot(
            [-L, L],  # 極大値に接する時の平行線y=B
            [cusp_value, cusp_value],
            label=f"y=B={cusp_value:.2f}",
            color="#00AA00",
            linewidth=LINE_WIDTH,
        )

        # plt.plot(
        #     [-x_h, -x_h],  # 縦棒
        #     [0, -cusp_value],
        #     # label=f"y=B=-{cusp_value:.2f}",
        #     color="#000000",
        #     linewidth=LINE_WIDTH,
        #     linestyle="--",
        # )
        # plt.plot(
        #     [-x_h],  # 極小値を取る時のx座標にマーカーを表示
        #     [0],
        #     "x",
        #     8,
        #     label=f"(x,y)=(0,{-x_h:.2f})",
        #     color="#0000AA",
        # )
        plt.plot(
            [-L, L],  # 極小値に接する時の平行線y=-B
            [-cusp_value, -cusp_value],
            label=f"y=B=-{cusp_value:.2f}",
            color="#0000AA",
            linewidth=LINE_WIDTH,
        )

    plt.legend(loc="lower center", borderaxespad=1, fontsize=10)


FRAMES = 1
FRAMES = 100
res = FuncAnimation(fig, draw, interval=100, frames=range(FRAMES))

# http://www.imagemagick.org/script/download.php#windowsのインストールが必要
# res.save(f"./cusp_anim_A=-2.gif", writer="imagemagick")
res.save(f"./new_cusp_anim.gif", writer="imagemagick")
