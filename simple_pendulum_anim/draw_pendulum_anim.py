import csv

# import seaborn as sns
from io import BytesIO
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
import pandas as pd
import numpy as np

# sns.set(style="darkgrid")

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
# ans_T = []
# ans_X = []
# ans_Y = []
frame_num = []
ans_eq_num = []
results = []
plt.axes().set_aspect("equal")

# file_name = "./ans_lotka_volterra_eq.csv"
file_name = "./ans_simple_pendulum_eq.csv"
with open(file_name, encoding="UTF-8") as f:
    reader = csv.reader(f)
    num = 0
    for line in reader:

        if num > 0:
            if num == 1:
                ans_theta = float(line[1])
                ans_omega = float(line[2])
            # ans_T.append(float(line[0]))
            # ans_X.append(float(line[1]))
            # ans_Y.append(float(line[2]))
            frame_num.append(int(line[3]))
            ans_eq_num.append(int(line[4]))
            results.append(
                {
                    "t": float(line[0]),
                    "theta": float(line[1]),
                    "omega": float(line[2]),
                    "frame_num": int(line[3]),
                    "eq_num": int(line[4]),
                }
            )
        # if num > 100:
        #     break
        num += 1
df = pd.DataFrame.from_dict(results, orient="columns")
max_frame_num = max(df["frame_num"].to_list())
max_eq_num = 1  # max(df["eq_num"].to_list())
# FRAMES = 40  # int(max_frame_num / 5)
FRAMES = 150


def get_data(df, pos: int, max_frame_num: int, max_eq_num: int):

    print(f"{max_frame_num=}, {max_eq_num=}")
    ret_x = []
    ret_y = []
    for num in range(max_eq_num):
        df2 = df[df["eq_num"] == num]
        df3 = df2[df2["frame_num"] == pos]
        # print(f"***{num=},{df3=}")
        ret_x.append(df3["theta"].to_list()[0])
        ret_y.append(df3["omega"].to_list()[0])
    return ret_x, ret_y


def create_frame(num: int):
    print(f"create_frame: {num=}****")
    plt.cla()

    plt.xlabel(r"$x$", fontsize=LABEL_FONT_SIZE)
    plt.ylabel(r"$y$", fontsize=LABEL_FONT_SIZE, rotation=0)
    # plt.grid(which="both", color=GRID_COLOR, linestyle="--", linewidth=GRID_LINE_WIDTH)

    plt.axhline(0, color=X_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.axvline(0, color=Y_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    AXIS_X_MAX = 1.5
    AXIS_Y_MAX = 1.5
    plt.xlim(-AXIS_X_MAX, AXIS_X_MAX)
    plt.ylim(-AXIS_Y_MAX, AXIS_Y_MAX)

    tmp_res = get_data(
        df=df, pos=num, max_frame_num=max_frame_num, max_eq_num=max_eq_num
    )
    r = 1.0
    x0 = [0]
    y0 = [0]
    plt.scatter(x0, y0, color="black")
    theta = tmp_res[0][0]
    x = np.linspace(0, r, 20)
    y = 0 * x

    x2 = np.cos(theta) * x + np.sin(theta) * y
    y2 = np.sin(theta) * x + np.cos(theta) * y

    x3 = y2
    y3 = -x2
    plt.plot(x3, y3, color="#FF0000")
    x3e = x3[::-1][0]
    y3e = y3[::-1][0]
    r_angle = 0.6 * r

    plt.plot(
        x3e,
        y3e,
        "o",
        ms=5,
        color="blue",
        label=rf"$\theta_{{0}}={ans_theta:.3f},\omega_{{0}}={ans_omega:.3f}$",
    )
    theta_list = np.linspace(0, theta, 100)
    circle_x = r_angle * np.cos(theta_list) + x0
    circle_y = r_angle * np.sin(theta_list) + y0

    circle_x2 = circle_y
    circle_y2 = -1.0 * circle_x
    plt.plot(circle_x2, circle_y2, color="gray", linestyle="-.")
    plt.text(
        circle_x2[0] + 0.3,
        circle_y2[0] - 0.6,
        rf"$\theta={theta:.3f}$ rad",
        color="gray",
        fontsize=14,
    )
    plt.legend(loc="upper center", borderaxespad=1, fontsize=12)

    buf = BytesIO()
    fig.savefig(buf)
    return Image.open(buf)


images = [create_frame(num) for num in range(4, FRAMES)]
images[0].save(
    "./pendulum_anim.gif",
    save_all=True,
    append_images=images[1:],
    duration=100,
    loop=0,
)
