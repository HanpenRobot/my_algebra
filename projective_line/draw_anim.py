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
AXIS_MAX = 10
TITLE_FONT_SIZE = 14
LABEL_FONT_SIZE = 16
N = 100
fig = plt.figure(dpi=256)

plt.axes().set_aspect("equal")


def draw(t: int):
    print(f"plotting {t=} ...")
    plt.cla()
    plt.title(f"Projective line: {t=}, {N=}", fontsize=TITLE_FONT_SIZE)
    plt.xlabel("X", fontsize=LABEL_FONT_SIZE)
    plt.ylabel("Y", fontsize=LABEL_FONT_SIZE)
    plt.grid(which="both", color=GRID_COLOR, linestyle="--", linewidth=GRID_LINE_WIDTH)

    plt.axhline(0, color=X_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.axvline(0, color=Y_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.xlim(-AXIS_MAX, AXIS_MAX)
    plt.ylim(-AXIS_MAX, AXIS_MAX)

    delta = 2 * np.pi / N
    theta = t * delta
    L = 20

    # X=1の直線をプロット
    plt.plot([1, 1], [-L, L], label="X=1", color=X1_LINE_COLOR, linewidth=LINE_WIDTH)

    # X=1と射影直線の交点をプロット
    plt.plot([1], [np.tan(theta)], "D", 8, color=X1_LINE_COLOR)

    # Y=1の直線をプロット
    plt.plot([-L, L], [1, 1], label="Y=1", color=Y1_LINE_COLOR, linewidth=LINE_WIDTH)

    # Y=1と射影直線の交点をプロット
    plt.plot([1 / np.tan(theta)], [1], "D", 8, color=Y1_LINE_COLOR)

    # 1次元射影直線をプロットする
    alpha = 10
    tmp_x = alpha * np.cos(theta)
    tmp_y = alpha * np.sin(theta)
    plt.plot(
        [-tmp_x, tmp_x],
        [-tmp_y, tmp_y],
        label=r"Y=$\tan(\frac{2\pi}{N} t)X$",
        color=PJ_LINE_COLOR,
        linewidth=LINE_WIDTH,
    )

    plt.legend(loc="lower center", borderaxespad=1, fontsize=10)


res = FuncAnimation(fig, draw, interval=100, frames=range(N))

# http://www.imagemagick.org/script/download.php#windowsのインストールが必要
res.save("projective_line_plot.gif", writer="imagemagick")
