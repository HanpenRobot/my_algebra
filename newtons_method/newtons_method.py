import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

PJ_LINE_COLOR = "#0000FF"
X1_LINE_COLOR = "#FF0000"
Y1_LINE_COLOR = "#00AA00"
X_AXIS_LINE_COLOR = "#000000"
Y_AXIS_LINE_COLOR = "#000000"
GRID_COLOR = "#444444"

LINE_WIDTH = 2
AXIS_LINE_WIDTH = 0.8
GRID_LINE_WIDTH = 0.8


FIGURE_SIZE = (10, 10)
TITLE_FONT_SIZE = 14
LABEL_FONT_SIZE = 16

fig = plt.figure(dpi=256)


# plt.axes().set_aspect("equal")
def func01(x: float) -> float:
    return x**3 - 2


def d_func01(x: float) -> float:
    return 3 * x**2


def newton_map(x: float) -> float:
    return x - (func01(x) / d_func01(x))


def draw(frame_num: int):
    print(f"plotting {frame_num=} ...")
    plt.cla()
    plt.xlabel("x", fontsize=LABEL_FONT_SIZE)
    plt.ylabel("y", fontsize=LABEL_FONT_SIZE)
    plt.grid(which="both", color=GRID_COLOR, linestyle="--", linewidth=GRID_LINE_WIDTH)

    plt.axhline(0, color=X_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.axvline(0, color=Y_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.xlim(1, 2.5)
    plt.ylim(-1, 15)
    step_size = 0.01
    X = []
    x = -6
    for num in range(2400):
        X.append(x)
        x += step_size
    Y = [func01(x) for x in X]

    plt.plot(X, Y, label=r"$y=x^3-2$", color="#FF0000", linewidth=2)

    x_init = 2.4
    x_res = x_init
    plt.plot([x_res], [0], markersize=4, color="#FF0000", marker="s", label=r"$x_n$")
    for num in range(frame_num):
        plt.plot([x_res], [0], markersize=4, color="#FF0000", marker="s")

        plt.plot([x_res], [func01(x_res)], markersize=4, color="#000000", marker="x")
        x_res_before = x_res
        x_res = newton_map(x_res)
        plt.plot(
            [x_res_before, x_res],
            [func01(x_res_before), 0],
            color="#0000FF",
            linewidth=1,
        )
        plt.plot(
            [x_res_before, x_res_before],
            [0, func01(x_res_before)],
            color="#0000FF",
            linewidth=1,
            linestyle="-.",
        )
    plt.title(
        rf"Newton's method for $2^{{\frac{{1}}{{3}}}}$ ($x_{{{frame_num}}}$={x_res:.11f})",
        fontsize=TITLE_FONT_SIZE,
    )

    plt.legend(loc="upper center", borderaxespad=1, fontsize=10)


N = 20
res = FuncAnimation(fig, draw, interval=100, frames=range(N))

# http://www.imagemagick.org/script/download.php#windowsのインストールが必要
res.save("newton_map001.gif", writer="imagemagick")
