import csv
import seaborn as sns
from io import BytesIO
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
import numpy as np

sns.set(style="darkgrid")

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
# N = 100
fig = plt.figure(dpi=256)
ans_T = []
ans_X = []
ans_Y = []
file_name = "./ans_duffing_eq_poincare.csv"
# ルンゲ・クッタ法のstepsizeが h = 0.0005
# なので、2pi / 0.0005 = 2*3.14 / 0.0005 = 6280 毎にx-yをよぎる点がポアンカレ写像の点

period = 6.28 / 0.0005
P_COUNT = 0
with open(file_name, encoding="UTF-8") as f:
    reader = csv.reader(f)
    num = 0

    for line in reader:
        if num > 0 and num % period == 0:

            ans_T.append(float(line[0]))
            ans_X.append(float(line[1]))
            ans_Y.append(float(line[2]))
            P_COUNT += 1
        num += 1
        # if P_COUNT > 10:
        #     break


def create_frame(num: int):
    print(f"frame_num: {num=}")
    plt.cla()

    plt.xlabel(r"$x$", fontsize=LABEL_FONT_SIZE)
    plt.ylabel(r"$y$", fontsize=LABEL_FONT_SIZE)
    plt.grid(which="both", color=GRID_COLOR, linestyle="--", linewidth=GRID_LINE_WIDTH)

    plt.axhline(0, color=X_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.axvline(0, color=Y_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    # AXIS_X_MAX = 3.14 * 9
    plt.xlim(2, 4)
    plt.ylim(-10, 10)
    # plt.xticks(
    #     np.arange(0, AXIS_X_MAX, 2 * np.pi),
    #     [0, r"$2\pi$", r"$4\pi$", r"$6\pi$", r"$8\pi$"],
    # )

    # Duffing方程式の解曲線をプロット
    plt.plot(
        ans_X,
        ans_Y,
        color=X1_LINE_COLOR,
        linestyle="None",
        marker="o",
        markersize=1,
        # marker="o", markersize=1, linestyle=None
    )
    plt.title(rf"Poincare's plot", fontsize=12, loc="center")
    plt.close()

    buf = BytesIO()
    fig.savefig(buf)
    return Image.open(buf)


FRAMES = 90
FRAMES = 180
FRAMES = 2
images = [create_frame(angle) for angle in range(FRAMES)]
images[0].save(
    "./poincare_xy_plot001.gif",
    save_all=True,
    append_images=images[1:],
    duration=100,
    loop=0,
)
