import csv
import seaborn as sns
from io import BytesIO
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image

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
file_name = "./ans_lotka_volterra_eq.csv"
with open(file_name, encoding="UTF-8") as f:
    reader = csv.reader(f)
    num = 0
    for line in reader:
        # if num > 0 and num % 500 == 0:
        # if num > 0:
        if num > 0 and num % 50 == 0:
            ans_T.append(float(line[0]))
            ans_X.append(float(line[1]))
            ans_Y.append(float(line[2]))
        num += 1

FRAMES = 360
# step_size = int(len(ans_X) / FRAMES)
# FRAMES -= 1


def create_frame(num: int):

    plt.cla()

    plt.xlabel(r"$x$", fontsize=LABEL_FONT_SIZE)
    plt.ylabel(r"$y$", fontsize=LABEL_FONT_SIZE)
    plt.grid(which="both", color=GRID_COLOR, linestyle="--", linewidth=GRID_LINE_WIDTH)

    plt.axhline(0, color=X_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.axvline(0, color=Y_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.xlim(0, 5)
    plt.ylim(0, 15)
    step_size = len(ans_X) / FRAMES
    pos = int(step_size * num)
    # pos = num
    # pos = (num - 1) * step_size
    # pos2 = num * step_size
    print(f"frame_num: {num=},{step_size=}, {pos=}***")
    # ans_T = []
    # ans_X = []
    # ans_Y = []
    # file_name = "./ans_duffing_eq.csv"
    # with open(file_name, encoding="UTF-8") as f:
    #     reader = csv.reader(f)
    #     num = 0
    #     for line in reader:
    #         if num > 0:
    #             ans_T.append(float(line[0]))
    #             ans_X.append(float(line[1]))
    #             ans_Y.append(float(line[2]))
    #         num += 1
    #         if num > pos:
    #             print(f"why={num=}*************")
    #             break

    # Lotka Volterra方程式の解曲線をプロット
    plt.plot(
        ans_X[:pos],
        ans_Y[:pos],
        color=X1_LINE_COLOR,
        # markersize=1,
        # marker="s",
        # linestyle="None",
    )

    # plt.close()

    buf = BytesIO()
    fig.savefig(buf)
    return Image.open(buf)


# FRAMES = 90
# FRAMES = 180
# FRAMES = 2

images = [create_frame(angle) for angle in range(2, FRAMES)]
images[0].save(
    "./lotka_volterra_plot_anim.gif",
    save_all=True,
    append_images=images[1:],
    duration=100,
    loop=0,
)
