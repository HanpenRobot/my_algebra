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
AXIS_MAX = 30
AXIS_MIN = 0.0
TITLE_FONT_SIZE = 14
LABEL_FONT_SIZE = 20

FRAMES = 100
CONST_A = 3.2
INIT_VALUE = 0.63
fig = plt.figure(dpi=256)

plt.axes().set_aspect("equal")


def get_cusp3(t: float):
    return (3.0 * t**2, 2.0 * t**3)


def draw(n: int):
    print(f"plotting {n=} ...")
    plt.cla()
    plt.xlabel(r"$A$", fontsize=LABEL_FONT_SIZE)
    plt.ylabel(r"$B$", fontsize=LABEL_FONT_SIZE)
    plt.grid(which="both", color=GRID_COLOR, linestyle="--", linewidth=GRID_LINE_WIDTH)

    plt.axhline(0, color=X_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.axvline(0, color=Y_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.xlim(-AXIS_MAX, AXIS_MAX)
    plt.ylim(-AXIS_MAX, AXIS_MAX)
    L = 20
    T = list(np.arange(-L, L, 0.1))
    results = []
    X = []
    Y = []
    for t in T:
        res = get_cusp3(t)
        print(f"{res=}")
        X.append(res[0])
        Y.append(res[1])

    plt.plot(
        X,
        Y,
        label=r"$(A,B)=(3u^2,2u^3), (-\infty < u < \infty)$",
        color=RT_LINE_COLOR,
        linewidth=LINE_WIDTH,
    )
    # 3価関数の領域を黄色で塗りつぶす
    plt.fill_between(X, Y, fc="yellow", label=r"3-valued area")

    plt.legend(loc="lower center", borderaxespad=1, fontsize=10)


FRAMES = 1
res = FuncAnimation(fig, draw, interval=100, frames=range(FRAMES))

# http://www.imagemagick.org/script/download.php#windowsのインストールが必要
res.save(f"./draw_cusp_area.gif", writer="imagemagick")
