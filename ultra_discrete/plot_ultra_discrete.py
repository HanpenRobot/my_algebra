import csv
from io import BytesIO
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
from matplotlib.animation import FuncAnimation
import numpy as np

FRAMES = 180
# fig = plt.figure(dpi=256)
fig = plt.figure(dpi=128)

# ans_X = []
# ans_Y = []

# file_name = "./ans_4d_poincare.csv"
# with open(file_name, encoding="UTF-8") as f:
#     reader = csv.reader(f)
#     num = 0
#     for line in reader:
#         if num > 0:
#             # // (x,w)=(\dot{Q1},Q1)は// 1,4
#             ans_X.append(float(line[4]))
#             ans_Y.append(float(line[1]))
#             # wがQ1, zがQ2,
#             # y, z が2, 3だから3,2 は (z, y) = (Q2,\dot{Q2}) = (Q2, P2)をプロットしている

#             # ans_X.append(float(line[3]))
#             # ans_Y.append(float(line[2]))
#             # # wがQ1, zがQ2,
#             # # y, z が2, 3だから3,2 は (z, y) = (Q2,\dot{Q2}) = (Q2, P2)をプロットしている
#         num += 1


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
    # plt.xticks(np.linspace(0, 4.2, 22))
    plt.axhline(0, color=X_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.axvline(0, color=Y_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.xlim(X_AXIS_MIN, X_AXIS_MAX)
    plt.ylim(Y_AXIS_MIN, Y_AXIS_MAX)

    ansX = np.linspace(0, Y_LIM, 30)
    epsilon = 1.0 / n
    ansY = np.log(np.exp(ansX / epsilon) + np.exp((0 * ansX + 3) / epsilon)) * epsilon
    # print(f"***{ansX=}")
    # print(f"aa{ansY=}")
    # x2 = np.cos(theta) * x + np.sin(theta) * y
    # y2 = np.sin(theta) * x + np.cos(theta) * y
    plt.plot(ansX, ansY, color=RT_LINE_COLOR)
    # plt.legend(loc="lower center", borderaxespad=1, fontsize=10)
    buf = BytesIO()
    fig.savefig(buf)
    return Image.open(buf)


FRAMES = 300
FRAMES = 10
res = FuncAnimation(fig, draw, interval=50, frames=range(2, FRAMES))

# http://www.imagemagick.org/script/download.php#windowsのインストールが必要
res.save(f"plot_ultra_discrete.gif", writer="imagemagick")
