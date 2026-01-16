import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

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
AXIS_MAX = 1.0
AXIS_MIN = 0.0
TITLE_FONT_SIZE = 14
LABEL_FONT_SIZE = 16
N = 20
CONST_A = 2.8
# N = 300
# CONST_A = 4


fig = plt.figure(dpi=256)

plt.axes().set_aspect("equal")


def func(x: float, CONST_A: float) -> float:
    """ロジスティック写像の値を求める"""
    return CONST_A * x * (1 - x)


def draw_return_map(init_value: float, n: int, CONST_A: float):
    ansX = [init_value]
    tmp_X = init_value
    X = func(x=tmp_X, CONST_A=CONST_A)
    ansX.append(X)
    # get logistic map value
    for num in range(n):
        tmp_X = X
        X = func(x=tmp_X, CONST_A=CONST_A)
        ansX.append(X)
    N_max = 200
    tmp_arry = [x / N for x in range(N_max + 1)]
    tmp_graph_Y = [func(x=x, CONST_A=CONST_A) for x in tmp_arry]
    plt.plot(  # plot logistic map
        tmp_arry,
        tmp_graph_Y,
        label=f"$y={CONST_A}x(1-x)$",
        color=CURVE_LINE_COLOR,
        linewidth=LINE_WIDTH,
    )
    plt.plot(  # plot y=x
        tmp_arry,
        tmp_arry,
        label=r"$y=x$",
        color=XY_LINE_COLOR,
        linewidth=LINE_WIDTH,
    )

    # draw return map
    for num in range(len(ansX) - 3):
        plt.plot(  # draw horizontal line --->
            [ansX[num], ansX[num + 1]],
            [ansX[num + 1], ansX[num + 1]],
            color=RT_LINE_COLOR,
            linewidth=LINE_WIDTH,
        )
        if num == 0:
            plt.plot(  # draw vertical line
                [ansX[num], ansX[num]],
                [0, ansX[num + 1]],
                color=RT_LINE_COLOR,
                linewidth=LINE_WIDTH,
            )
        else:
            plt.plot(  # vertical line
                [ansX[num], ansX[num]],
                [ansX[num], ansX[num + 1]],
                color=RT_LINE_COLOR,
                linewidth=LINE_WIDTH,
            )


def draw(n: int):
    print(f"plotting {n=} ...")
    plt.cla()
    plt.title(f"Return map ${n=}$", fontsize=TITLE_FONT_SIZE)
    plt.xlabel(r"$X_n$", fontsize=LABEL_FONT_SIZE)
    plt.ylabel(r"$X_{n+1}$", fontsize=LABEL_FONT_SIZE)
    plt.grid(which="both", color=GRID_COLOR, linestyle="--", linewidth=GRID_LINE_WIDTH)

    plt.axhline(0, color=X_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.axvline(0, color=Y_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.xlim(0, AXIS_MAX)
    plt.ylim(0, AXIS_MAX)
    init_value = 0.2
    draw_return_map(init_value=init_value, n=n, CONST_A=CONST_A)
    plt.legend(loc="lower center", borderaxespad=1, fontsize=10)


res = FuncAnimation(fig, draw, interval=100, frames=range(N))

# http://www.imagemagick.org/script/download.php#windowsのインストールが必要
res.save(f"logistic_map_{CONST_A}.gif", writer="imagemagick")
