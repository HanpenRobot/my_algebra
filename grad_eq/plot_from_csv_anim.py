import csv
from io import BytesIO
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
from matplotlib.animation import FuncAnimation
import numpy as np

FRAMES = 180
# fig = plt.figure(dpi=256)
fig = plt.figure(dpi=128)

ans_X = []
ans_Y = []

file_name = "./ans_grad.csv"
with open(file_name, encoding="UTF-8") as f:
    reader = csv.reader(f)
    num = 0
    for line in reader:
        if num > 0:
            # if num > 0:
            # ans_X.append(float(line[2]))
            # ans_Y.append(float(line[4]))
            ans_X.append(float(line[1]))
            ans_Y.append(float(line[3]))
        num += 1


def draw(n: int):

    print(f"plotting {n=} ...")
    N_max = 2000
    limit_const = 0.7
    CURVE_LINE_COLOR = "#0000FF"
    RT_LINE_COLOR = "#FF0000"
    XY_LINE_COLOR = "#00AA00"
    X_AXIS_LINE_COLOR = "#000000"
    Y_AXIS_LINE_COLOR = "#000000"
    GRID_COLOR = "#444444"

    LINE_WIDTH = 1
    AXIS_LINE_WIDTH = 0.8
    GRID_LINE_WIDTH = 0.8

    FIGURE_SIZE = (5, 5)
    X_LIM = 80
    Y_LIM = 80
    Y_AXIS_MAX = X_LIM
    Y_AXIS_MIN = -X_LIM
    X_AXIS_MAX = Y_LIM
    X_AXIS_MIN = -Y_LIM

    TITLE_FONT_SIZE = 14
    LABEL_FONT_SIZE = 16
    plt.axes().set_aspect("equal")
    plt.cla()
    plt.xlabel(r"$x$", fontsize=LABEL_FONT_SIZE)
    plt.ylabel(r"$y$", fontsize=LABEL_FONT_SIZE, rotation=0)
    plt.grid(which="both", color=GRID_COLOR, linestyle="--", linewidth=GRID_LINE_WIDTH)
    # plt.xticks(np.linspace(0, 4.2, 22))
    plt.axhline(0, color=X_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.axvline(0, color=Y_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.xlim(X_AXIS_MIN, X_AXIS_MAX)
    plt.ylim(Y_AXIS_MIN, Y_AXIS_MAX)

    plt.plot(ans_X[:n], ans_Y[:n], "o", ms=1, color=RT_LINE_COLOR)
    # plt.legend(loc="lower center", borderaxespad=1, fontsize=10)
    buf = BytesIO()
    fig.savefig(buf)
    return Image.open(buf)


FRAMES = 300
FRAMES = 250
res = FuncAnimation(fig, draw, interval=50, frames=range(FRAMES))

# http://www.imagemagick.org/script/download.php#windowsのインストールが必要
res.save(f"plot_grad_anim.gif", writer="imagemagick")
