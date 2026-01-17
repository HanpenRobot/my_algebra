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
Y_AXIS_MAX = 1.5
Y_AXIS_MIN = 0.0
X_AXIS_MAX = 4.5
X_AXIS_MIN = 1.0

TITLE_FONT_SIZE = 14
LABEL_FONT_SIZE = 16


fig = plt.figure(dpi=256)

plt.axes().set_aspect("equal")


def func(x: float, CONST_A: float) -> float:
    """ロジスティック写像の値を求める"""
    return CONST_A * x * (1 - x)


def get_limit_value(init_value: float, CONST_A, N_max: int, limit_const: int):

    ansX = [init_value]
    tmp_X = init_value
    X = func(x=tmp_X, CONST_A=CONST_A)
    ansX.append(X)
    # get logistic map value
    for num in range(N_max):
        tmp_X = X
        X = func(x=tmp_X, CONST_A=CONST_A)
        ansX.append(X)
    tmp_res = list(set(ansX[int(N_max * limit_const) :]))
    res = []
    for value in tmp_res:
        res.append((CONST_A, value))  # x[inf] limit value ( N -> inf )
    return res


def draw(n: int):
    print(f"plotting {n=} ...")
    N_max = 2000
    limit_const = 0.7
    plt.cla()
    plt.xlabel(r"$\alpha$", fontsize=LABEL_FONT_SIZE)
    plt.ylabel(rf"$x_n$, $(n > {int(N_max * limit_const)})$", fontsize=LABEL_FONT_SIZE)
    plt.grid(which="both", color=GRID_COLOR, linestyle="--", linewidth=GRID_LINE_WIDTH)

    plt.axhline(0, color=X_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.axvline(0, color=Y_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.xlim(X_AXIS_MIN, X_AXIS_MAX)
    plt.ylim(Y_AXIS_MIN, Y_AXIS_MAX)
    N_max = 10
    start_CONST_A = 1.0
    end_CONST_A = 4.2
    plt.title(
        rf"bifurcation plot {start_CONST_A} < $\alpha$ < {end_CONST_A:.2f}",
        fontsize=TITLE_FONT_SIZE,
    )

    init_value = 0.2
    tmp_res = []
    CONST_LIST = []
    tmp_const = start_CONST_A
    delta = 0.02
    for x in range(10 * n):
        CONST_LIST.append(tmp_const)
        if tmp_const > end_CONST_A:
            break
        tmp_const += delta

    for CONST_A in CONST_LIST:
        tmp_res += get_limit_value(
            init_value=init_value, CONST_A=CONST_A, N_max=N_max, limit_const=limit_const
        )
    tmp_res_X = []
    tmp_res_Y = []
    for item in tmp_res:
        tmp_res_X.append(item[0])
        tmp_res_Y.append(item[1])
    # (CONST_A、x[n])にプロットする ( n > N_max*limit_const )
    plt.plot(tmp_res_X, tmp_res_Y, "o", ms=2, color=RT_LINE_COLOR)
    plt.legend(loc="lower center", borderaxespad=1, fontsize=10)


FRAMES = 30
res = FuncAnimation(fig, draw, interval=50, frames=range(FRAMES))

# http://www.imagemagick.org/script/download.php#windowsのインストールが必要
res.save(f"bifurcation.gif", writer="imagemagick")
