import csv
import seaborn as sns
from io import BytesIO
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
import pandas as pd

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
frame_num = []
ans_eq_num = []
results = []


# file_name = "./ans_lotka_volterra_eq.csv"
file_name = "./ans_lotka_volterra_eq3.csv"
with open(file_name, encoding="UTF-8") as f:
    reader = csv.reader(f)
    num = 0
    for line in reader:

        if num > 0:
            ans_T.append(float(line[0]))
            ans_X.append(float(line[1]))
            ans_Y.append(float(line[2]))
            frame_num.append(int(line[3]))
            ans_eq_num.append(int(line[4]))
            results.append(
                {
                    "t": float(line[0]),
                    "x": float(line[1]),
                    "y": float(line[2]),
                    "frame_num": int(line[3]),
                    "eq_num": int(line[4]),
                }
            )
        # if num > 100:
        #     break
        num += 1
df = pd.DataFrame.from_dict(results, orient="columns")
max_frame_num = max(df["frame_num"].to_list())
max_eq_num = max(df["eq_num"].to_list())
FRAMES = 40  # int(max_frame_num / 5)


def get_data(df, pos: int, max_frame_num: int, max_eq_num: int):

    print(f"{max_frame_num=}, {max_eq_num=}")
    ret_x = []
    ret_y = []
    for num in range(max_eq_num):
        df2 = df[df["eq_num"] == num]
        df3 = df2[df2["frame_num"] == pos]
        # print(f"***{num=},{df3=}")
        ret_x.append(df3["x"].to_list()[0])
        ret_y.append(df3["y"].to_list()[0])
    return ret_x, ret_y


def create_frame(num: int):
    print(f"create_frame: {num=}****")
    plt.cla()

    plt.xlabel(r"$x$", fontsize=LABEL_FONT_SIZE)
    plt.ylabel(r"$y$", fontsize=LABEL_FONT_SIZE)
    plt.grid(which="both", color=GRID_COLOR, linestyle="--", linewidth=GRID_LINE_WIDTH)

    plt.axhline(0, color=X_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.axvline(0, color=Y_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.xlim(-1, 7)
    plt.ylim(-1, 7)
    plt.title(
        # r"$\frac{{dx}}{{dt}}=(K1-ax-by)x, (K_1=6, a=2, b=1)$ \n $\frac{{dy}}{{dt}}=-(K2-cx-dy)y, (K_2=10, c=2, d=6)$",
        r"$\frac{dx}{dt}=(K_1-ax-by)x, (K_1=6, a=2, b=1)$"
        + "\n"
        + r"$\frac{dy}{dt}=(K_2-cx-dy)y, (K_2=5, c=1, d=3)$",
        fontsize=10,
        loc="center",
    )

    # ```math
    # \frac{dx}{dt}=(K1-ax-by)x, (K_1=6, a=2, b=1) \cdots (1)
    # ```

    # ```math
    # \frac{dy}{dt}=-(K2-cx-dy)y, (K_2=10, c=2, d=6) \cdots (2)
    # ```
    # step_size = max_frame_num / FRAMES
    pos = num
    # int(step_size * num)
    res = get_data(df=df, pos=pos, max_frame_num=max_frame_num, max_eq_num=max_eq_num)
    plt.plot(
        res[0],
        res[1],
        color=X1_LINE_COLOR,
        markersize=1,
        marker="s",
        linestyle="None",
    )
    a = 2
    b = 1
    c = 1
    d = 3
    K1 = 6
    K2 = 5
    plt.plot(
        [K1 / a, 0],
        [0, K1 / b],
        color="#0000FF",
        markersize=1,
        marker="s",
        linestyle="-.",
        label=r"$K_1=ax+by$",
    )

    plt.plot(
        [K2 / c, 0],
        [0, K2 / d],
        color="#00AA00",
        markersize=1,
        marker="s",
        linestyle="-.",
        label=r"$K_2=cx+dy$",
    )

    tmp_det = a * d - b * c
    P_star = ((d * K1 - b * K2) / tmp_det, (a * K2 - c * K1) / tmp_det)
    plt.plot(
        [P_star[0]],
        [P_star[1]],
        color="#FF00FF",
        markersize=5,
        marker="D",
        linestyle="None",
        label=rf"$P^{{*}}=({P_star[0]},{P_star[1]})$",
    )

    P1 = (K1 / a, 0)
    plt.plot(
        [P1[0]],
        [P1[1]],
        color="#F000FF",
        markersize=5,
        marker="^",
        linestyle="None",
        label=rf"$P^{{1}}=({P1[0]},{P1[1]})$",
    )

    P2 = (0, K2 / d)
    plt.plot(
        [P2[0]],
        [P2[1]],
        color="#F000FF",
        markersize=5,
        marker="v",
        linestyle="None",
        label=rf"$P^{{2}}=({P2[0]},{P2[1]:.3f})$",
    )
    P0 = (0, 0)
    plt.plot(
        [P0[0]],
        [P0[1]],
        color="#F000FF",
        markersize=5,
        marker="o",
        linestyle="None",
        label=rf"$P^{{0}}=({P0[0]},{P0[1]})$",
    )
    plt.legend(loc="upper center", borderaxespad=1, fontsize=8)
    # plt.close()

    buf = BytesIO()
    fig.savefig(buf)
    return Image.open(buf)


images = [create_frame(num) for num in range(4, FRAMES)]
images[0].save(
    "./vec_field_lotka_volterra_anim3.gif",
    save_all=True,
    append_images=images[1:],
    duration=100,
    loop=0,
)
