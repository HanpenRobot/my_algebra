import csv
from io import BytesIO
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
from matplotlib.animation import FuncAnimation
import numpy as np
import pandas as pd

FRAMES = 180
fig = plt.figure(dpi=256)


results = []
file_name = "./ans_henon_map_per.csv"
with open(file_name, encoding="UTF-8") as f:
    reader = csv.reader(f)
    num = 0
    for line in reader:
        if num > 0:

            results.append(
                {"a": float(line[0]), "b": float(line[1]), "per": int(line[2])}
            )
        num += 1

df = pd.DataFrame.from_dict(results, orient="columns")
print(f"***{df=}")


def make_data(tmp_df, per: int):
    tmp_df2 = tmp_df[tmp_df["per"] == per]
    tmp_A = tmp_df2["a"].to_list()
    tmp_B = tmp_df2["b"].to_list()
    return tmp_A, tmp_B


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
    Y_AXIS_MAX = 1.0
    Y_AXIS_MIN = -1.0
    X_AXIS_MAX = 2.0
    X_AXIS_MIN = 0.0

    TITLE_FONT_SIZE = 14
    LABEL_FONT_SIZE = 16
    plt.cla()
    plt.xlabel(r"$a$", fontsize=LABEL_FONT_SIZE)
    plt.ylabel(r"$b$", fontsize=LABEL_FONT_SIZE, rotation=0)
    plt.grid(which="both", color=GRID_COLOR, linestyle="--", linewidth=GRID_LINE_WIDTH)
    # plt.xticks(np.linspace(0, 4.2, 22))
    plt.axhline(0, color=X_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.axvline(0, color=Y_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.xlim(X_AXIS_MIN, X_AXIS_MAX)
    plt.ylim(Y_AXIS_MIN, Y_AXIS_MAX)

    res_A, res_B = make_data(tmp_df=df, per=1)
    plt.plot(res_A, res_B, ".", ms=1, color="#0000FF")

    res_A2, res_B2 = make_data(tmp_df=df, per=2)
    plt.plot(res_A2, res_B2, ".", ms=1, color="#00AA00")

    res_A3, res_B3 = make_data(tmp_df=df, per=3)
    plt.plot(res_A3, res_B3, ".", ms=1, color="#00AAAA")

    res_A4, res_B4 = make_data(tmp_df=df, per=4)
    plt.plot(res_A4, res_B4, ".", ms=1, color="#FF0000")

    res_A5, res_B5 = make_data(tmp_df=df, per=-1)
    plt.plot(res_A5, res_B5, ".", ms=1, color="#000000")

    res_A6, res_B6 = make_data(tmp_df=df, per=5)
    plt.plot(res_A6, res_B6, ".", ms=1, color="#AA00AA")

    # plt.legend(loc="lower center", borderaxespad=1, fontsize=10)


FRAMES = 1
res = FuncAnimation(fig, draw, interval=50, frames=range(FRAMES))

# http://www.imagemagick.org/script/download.php#windowsのインストールが必要
res.save(f"ans_henon_map_per.gif", writer="imagemagick")
