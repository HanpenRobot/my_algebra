import csv
from io import BytesIO
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
from matplotlib.animation import FuncAnimation
import numpy as np
import seaborn as sns
import pandas as pd

FRAMES = 180
fig = plt.figure(dpi=256)


results = []
ans_eq_num = []
frame_num = 0
file_name = "./ans_ca.csv"
with open(file_name, encoding="UTF-8") as f:
    reader = csv.reader(f, delimiter="\n")
    num = 0
    for line in reader:
        if num > 0:
            print(f"***{num=}, {line=}")
            tmp_ans_list = line[0].split(",")
            tmp_ans_list = [int(x) for x in tmp_ans_list]
            ans_list = tmp_ans_list[1:]
            frame_num = tmp_ans_list[0]
            ans_eq_num.append(frame_num)

            results.append(
                {
                    "ans_list": ans_list,
                    "frame_num": frame_num,
                }
            )

        num += 1
df = pd.DataFrame.from_dict(results, orient="columns")
max_frame_num = max(df["frame_num"].to_list())
print(f"*****************{df=}")


def get_data(
    tmp_df,
    pos: int,
):

    tmp_df2 = tmp_df[tmp_df["frame_num"] == pos]
    tmp_ret = tmp_df2["ans_list"].to_list()

    return tmp_ret


def draw(draw_num: int):

    print(f"plotting {draw_num=} ...")
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
    Y_LIM = 5.0
    Y_AXIS_MAX = Y_LIM
    Y_AXIS_MIN = 0
    X_AXIS_MAX = 6.5
    X_AXIS_MIN = 0

    TITLE_FONT_SIZE = 14
    LABEL_FONT_SIZE = 16
    plt.axes().set_aspect("equal")
    plt.cla()
    plt.xlabel(r"$X$", fontsize=LABEL_FONT_SIZE)
    plt.ylabel(r"$Y$", fontsize=LABEL_FONT_SIZE, rotation=0)
    plt.grid(which="both", color=GRID_COLOR, linestyle="--", linewidth=GRID_LINE_WIDTH)
    plt.axhline(0, color=X_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.axvline(0, color=Y_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.xlim(X_AXIS_MIN, X_AXIS_MAX)
    plt.ylim(Y_AXIS_MIN, Y_AXIS_MAX)
    ans_mat2d = get_data(tmp_df=df, pos=draw_num)

    sns.heatmap(
        ans_mat2d,
        cbar=False,
        square=True,
        cmap="Blues",
        xticklabels=False,
        yticklabels=False,
        linewidths=0.5,
        linecolor="gray",
        # , xticklabels=1, yticklabels=1
    )

    # plt.plot(ansX, ansY, color=RT_LINE_COLOR)
    # plt.legend(loc="lower center", borderaxespad=1, fontsize=10)
    buf = BytesIO()
    fig.savefig(buf)
    return Image.open(buf)


FRAMES = 300
FRAMES = max_frame_num
res = FuncAnimation(fig, draw, interval=50, frames=range(0, FRAMES))

# http://www.imagemagick.org/script/download.php#windowsのインストールが必要
res.save(f"plot_ca.gif", writer="imagemagick")
