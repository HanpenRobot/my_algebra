import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

PJ_LINE_COLOR = "#0000FF"
X1_LINE_COLOR = "#FF0000"
Y1_LINE_COLOR = "#00AA00"
X_AXIS_LINE_COLOR = "#000000"
Y_AXIS_LINE_COLOR = "#000000"
GRID_COLOR = "#444444"

LINE_WIDTH = 1
AXIS_LINE_WIDTH = 0.8
GRID_LINE_WIDTH = 0.8


FIGURE_SIZE = (10, 10)
AXIS_MAX = 1
TITLE_FONT_SIZE = 14
LABEL_FONT_SIZE = 16

fig = plt.figure(dpi=256)

plt.axes().set_aspect("equal")


def complex_func(z: complex):
    return z**2


def draw(t: int):
    print(f"plotting {t=} ...")
    plt.cla()
    plt.title(f"$f(z)=z^2$", fontsize=TITLE_FONT_SIZE)
    plt.xlabel(f"$\Re w$", fontsize=LABEL_FONT_SIZE)
    plt.ylabel(f"$\Im w$", fontsize=LABEL_FONT_SIZE)
    plt.grid(which="both", color=GRID_COLOR, linestyle="--", linewidth=GRID_LINE_WIDTH)

    plt.axhline(0, color=X_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.axvline(0, color=Y_AXIS_LINE_COLOR, linewidth=LINE_WIDTH)
    plt.xlim(-AXIS_MAX, AXIS_MAX)
    plt.ylim(-AXIS_MAX, AXIS_MAX)

    L = 3
    MAX = np.pi / 2
    STEP = MAX / 20

    theta = STEP * t
    tmp_M = complex(np.cos(theta), np.sin(theta))
    tmp_L = complex(-np.sin(theta), np.cos(theta))
    X = np.linspace(-L, L, 2 * L + 1)
    Y = np.linspace(-L, L, 2 * L + 1)

    plt.quiver(
        0,
        0,
        tmp_M.real,
        tmp_M.imag,
        color="#FF0000",
        angles="xy",
        scale_units="xy",
        scale=1,
    )
    plt.quiver(
        0,
        0,
        tmp_L.real,
        tmp_L.imag,
        color="#FF0000",
        angles="xy",
        scale_units="xy",
        scale=1,
    )
    tmp_M2 = tmp_M**2
    tmp_L2 = tmp_L**2
    plt.quiver(
        0,
        0,
        tmp_M2.real,
        tmp_M2.imag,
        color="#0000FF",
        angles="xy",
        scale_units="xy",
        scale=1,
    )
    plt.quiver(
        0,
        0,
        tmp_L2.real,
        tmp_L2.imag,
        color="#0000FF",
        angles="xy",
        scale_units="xy",
        scale=1,
    )
    # for x in X:
    #     for y in Y:
    #         z = complex(real=x, imag=y)
    #         res = complex_func(z)
    #         print(f"{x=}, {y=}, {z=}")
    #         plt.quiver(x, y, res.real, res.imag, color="#FF0000")


N = 20
res = FuncAnimation(fig, draw, interval=100, frames=range(N))

# http://www.imagemagick.org/script/download.php#windowsのインストールが必要
res.save("conformal.gif", writer="imagemagick")
