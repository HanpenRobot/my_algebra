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

ans_omega = []
ans_A = []
# ans_X = []

file_name = "./duffing_eq_result.csv"
with open(file_name, encoding="UTF-8") as f:
    reader = csv.reader(f)
    num = 0
    for line in reader:
        if num > 0:
            ans_omega.append(float(line[0]))
            ans_A.append(float(line[1]))
            # ans_X.append(float(line[2]))
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
    Y_AXIS_MAX = 5
    Y_AXIS_MIN = -0
    X_AXIS_MAX = 12
    X_AXIS_MIN = -12
    TITLE_FONT_SIZE = 14
    LABEL_FONT_SIZE = 16
    plt.cla()
    plt.xlabel(r"$\omega$", fontsize=LABEL_FONT_SIZE)
    plt.ylabel(r"$A$", fontsize=LABEL_FONT_SIZE)
    plt.grid(which="both", color=GRID_COLOR, linestyle="--", linewidth=GRID_LINE_WIDTH)
    plt.axhline(0, color=X_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.axvline(0, color=Y_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.xlim(X_AXIS_MIN, X_AXIS_MAX)
    plt.ylim(Y_AXIS_MIN, Y_AXIS_MAX)

    plt.plot(ans_omega, ans_A, "o", ms=1, color=RT_LINE_COLOR)
    # plt.legend(loc="lower center", borderaxespad=1, fontsize=10)


FRAMES = 1
res = FuncAnimation(fig, draw, interval=50, frames=range(FRAMES))
res.save(f"duffing_res.gif", writer="imagemagick")

# res = FuncAnimation(fig, draw2, interval=50, frames=range(FRAMES))
# res.save(f"relax_map_x_t.gif", writer="imagemagick")


# res = FuncAnimation(fig, draw3, interval=50, frames=range(FRAMES))
# res.save(f"relax_map_x_v.gif", writer="imagemagick")
