import csv
import seaborn as sns
from io import BytesIO
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
from matplotlib.animation import FuncAnimation
import numpy as np

sns.set(style="darkgrid")

FRAMES = 180
fig = plt.figure(dpi=256)

ans_X = []
ans_Y = []

file_name = "./ans_henon_map.csv"
with open(file_name, encoding="UTF-8") as f:
    reader = csv.reader(f)
    num = 0
    for line in reader:
        if num > 0:
            ans_X.append(float(line[0]))
            ans_Y.append(float(line[1]))
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

    FIGURE_SIZE = (10, 10)
    Y_AXIS_MAX = 0.5
    Y_AXIS_MIN = -0.5
    X_AXIS_MAX = 1.5
    X_AXIS_MIN = -1.5

    TITLE_FONT_SIZE = 14
    LABEL_FONT_SIZE = 16
    plt.cla()
    plt.xlabel(r"$x$", fontsize=LABEL_FONT_SIZE)
    plt.ylabel(r"$y$", fontsize=LABEL_FONT_SIZE)
    plt.grid(which="both", color=GRID_COLOR, linestyle="--", linewidth=GRID_LINE_WIDTH)
    # plt.xticks(np.linspace(0, 4.2, 22))
    plt.axhline(0, color=X_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.axvline(0, color=Y_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.xlim(X_AXIS_MIN, X_AXIS_MAX)
    plt.ylim(Y_AXIS_MIN, Y_AXIS_MAX)

    plt.plot(ans_X, ans_Y, "o", ms=1, color=RT_LINE_COLOR)
    # plt.legend(loc="lower center", borderaxespad=1, fontsize=10)


FRAMES = 1
res = FuncAnimation(fig, draw, interval=50, frames=range(FRAMES))

# http://www.imagemagick.org/script/download.php#windowsのインストールが必要
res.save(f"henon_map.gif", writer="imagemagick")
