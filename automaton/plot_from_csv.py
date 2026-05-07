import csv
import seaborn as sns
from io import BytesIO
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
from matplotlib.animation import FuncAnimation
import numpy as np

sns.set(style="darkgrid")
#

FRAMES = 180
fig = plt.figure(dpi=256)

ans_X = []
ans_Y = []

file_name = "./ans_automaton_pos.csv"
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
    Y_AXIS_MAX = 1000.0
    Y_AXIS_MIN = -1000.0
    X_AXIS_MAX = 1000.0
    X_AXIS_MIN = -1000.0

    TITLE_FONT_SIZE = 14
    LABEL_FONT_SIZE = 16
    # plt.cla()
    # plt.axes().set_aspect("equal")
    plt.axes().invert_yaxis()
    plt.xlabel(r"$a$", fontsize=LABEL_FONT_SIZE)
    plt.ylabel(r"$n$", fontsize=LABEL_FONT_SIZE)
    plt.grid(which="both", color=GRID_COLOR, linestyle="--", linewidth=GRID_LINE_WIDTH)
    # plt.xticks(np.linspace(0, 4.2, 22))
    plt.axhline(0, color=X_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.axvline(0, color=Y_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.xlim(X_AXIS_MIN, X_AXIS_MAX)
    plt.ylim(Y_AXIS_MIN, Y_AXIS_MAX)
    # 縦横比を1:1に設定

    plt.plot(ans_X, ans_Y, "o", ms=1.0, color=RT_LINE_COLOR)
    # plt.legend(loc="lower center", borderaxespad=1, fontsize=10)


# FRAMES = 1
# res = FuncAnimation(fig, draw, interval=50, frames=[1])

# # http://www.imagemagick.org/script/download.php#windowsのインストールが必要
# res.save(f"automaton_output.gif", writer="imagemagick")

# fig = plt.figure()
# plt.clf()


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
Y_AXIS_MAX = 100.0
Y_AXIS_MIN = 0.0
X_AXIS_MAX = 100.0
X_AXIS_MIN = 0.0

TITLE_FONT_SIZE = 14
LABEL_FONT_SIZE = 16
# plt.cla()
# plt.axes().set_aspect("equal")
plt.xlabel(r"$a$", fontsize=LABEL_FONT_SIZE)
plt.ylabel(r"$n$", fontsize=LABEL_FONT_SIZE)
plt.grid(which="both", color=GRID_COLOR, linestyle="--", linewidth=GRID_LINE_WIDTH)
# plt.xticks(np.linspace(0, 4.2, 22))
# plt.axhline(0, color=X_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
# plt.axvline(0, color=Y_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
plt.xlim(X_AXIS_MIN, X_AXIS_MAX)
plt.ylim(Y_AXIS_MIN, Y_AXIS_MAX)
# 縦横比を1:1に設定

plt.plot(ans_X, ans_Y, "s", ms=1.0, color=RT_LINE_COLOR)
plt.gca().invert_yaxis()

plt.savefig("ans001.png")
# plt.show()
# plt.gca().invert_yaxis()
