import csv
import seaborn as sns
from io import BytesIO
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
from matplotlib.animation import FuncAnimation
import numpy as np

sns.set(style="darkgrid")

# FRAMES = 18
fig = plt.figure(dpi=256)

FRAMES = 128


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
    N_max = 90000
    plt.xlabel(rf"$x_n$, $(n > {N_max})$", fontsize=LABEL_FONT_SIZE)
    plt.ylabel(rf"$y_n$, $(n > {N_max})$", fontsize=LABEL_FONT_SIZE)
    plt.grid(which="both", color=GRID_COLOR, linestyle="--", linewidth=GRID_LINE_WIDTH)
    plt.axhline(0, color=X_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.axvline(0, color=Y_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.xlim(X_AXIS_MIN, X_AXIS_MAX)
    plt.ylim(Y_AXIS_MIN, Y_AXIS_MAX)

    tmp_ans_X = []
    tmp_ans_Y = []
    tmp_ans_A = []
    file_name = "./ans_henon_map_anim.csv"
    with open(file_name, encoding="UTF-8") as f:
        reader = csv.reader(f)
        num = 0
        for line in reader:
            if num > 0:
                if int(line[3]) == n:
                    tmp_ans_X.append(float(line[0]))
                    tmp_ans_Y.append(float(line[1]))
                    tmp_ans_A.append(float(line[2]))

            num += 1
    plt.title(
        rf"a={tmp_ans_A[0]:.2f},b=0.3",
        fontsize=TITLE_FONT_SIZE,
    )

    plt.plot(tmp_ans_X, tmp_ans_Y, "o", ms=1, color=RT_LINE_COLOR)
    # plt.legend(loc="lower center", borderaxespad=1, fontsize=10)


res = FuncAnimation(fig, draw, interval=50, frames=range(FRAMES))

# http://www.imagemagick.org/script/download.php#windowsのインストールが必要
res.save(f"henon_map_anim2.gif", writer="imagemagick")
