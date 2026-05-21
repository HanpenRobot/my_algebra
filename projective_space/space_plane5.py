import csv
import seaborn as sns
from io import BytesIO
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
import numpy as np

sns.set(style="darkgrid")


def create_frame(angle: int):
    print(f"{angle=}")

    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection="3d")

    L = 3
    TMP_ARRY = np.linspace(-L, L, 2 * L + 1)
    x = TMP_ARRY
    y = TMP_ARRY
    X, Y = np.meshgrid(x, y)
    # ax.plot_surface(X, Y, Z=X * 0 + 1.0, color="#00AA00", alpha=0.3)
    # ax.plot_surface(X, Y=X * 0 + 1.0, Z=Y, color="y", alpha=0.3)

    # ax.plot_surface(X=X * 0 + 1.0, Y=Y, Z=X, color="r", alpha=0.3)

    # 矢幅・矢長比・矢頭長比を指定
    lw = 3
    l = 1.0
    alr = 0.1

    ax.quiver(  # Z軸の矢印
        0,
        0,
        0,
        0,
        0,
        5,
        length=l,
        arrow_length_ratio=alr,
        color="#000000",
        linewidth=lw,
    )

    ax.quiver(  # Y軸の矢印
        0,
        0,
        0,
        0,
        5,
        0,
        length=l,
        arrow_length_ratio=alr,
        color="#000000",
        linewidth=lw,
    )

    ax.quiver(  # X軸の矢印
        0,
        0,
        0,
        5,
        0,
        0,
        length=l,
        arrow_length_ratio=alr,
        color="#000000",
        linewidth=lw,
    )

    # y=x^2
    # (Y/Z)=(X/Z)^2
    # Y/Z = X^2 / Z^2
    # ZY=X^2
    # Z=1 -> Y=X^2
    # Y=1 -> Z=X^2
    # X=1 -> ZY=1 -> Y = 1/Z
    num = angle
    TMP_ARRY2 = np.linspace(-L, L, 20 * L + 1)
    # 放物線の値を生成 Z=1 -> Y=X^2
    graph_x = TMP_ARRY2
    graph_y = TMP_ARRY2**2
    graph_z = TMP_ARRY2 * 0 + 1.0
    tmp_value = TMP_ARRY2[num]
    sc = ax.plot(graph_x, graph_y, graph_z, linewidth=3, c="#FF0000", marker=None)
    sc = ax.plot(
        tmp_value,
        tmp_value**2,
        1.0,
        markersize=12,
        c="#FF0000",
        label=r"$(X,Y,Z)=(t,t^2,1)$",
        marker="o",
    )

    # 放物線の値を生成 Y=1 -> Z=X^2
    graph_x2 = TMP_ARRY2
    graph_y2 = TMP_ARRY2 * 0 + 1.0
    graph_z2 = TMP_ARRY2**2
    sc = ax.plot(graph_x2, graph_y2, graph_z2, linewidth=3, c="#00AA00", marker=None)
    sc = ax.plot(
        1.0 / tmp_value,
        1.0,
        1.0 / (tmp_value**2),
        label=r"$(X,Y,Z)=(t,1,t^2)$",
        markersize=12,
        c="#00AA00",
        marker="o",
    )

    TMP_ARRY3 = np.linspace(-2 * L, 2 * L, 40 * L + 1)
    # 放物線の値を生成 X=1 -> ZY=1 -> Y = 1/Z
    graph_x3 = TMP_ARRY3 * 0 + 1.0
    graph_y3 = 1 / TMP_ARRY3
    graph_z3 = TMP_ARRY3
    sc = ax.plot(graph_x3, graph_y3, graph_z3, linewidth=3, c="#0000FF", marker=None)
    sc = ax.plot(
        1.0,
        tmp_value,
        1.0 / tmp_value,
        c="#0000FF",
        label=r"$(X,Y,Z)=(1,\frac{1}{t},t)$",
        markersize=12,
        marker="o",
    )

    alpha = 5.0
    line_length = 2
    tmp_value2 = tmp_value
    ax.quiver(  # 原点を通る直線
        0,
        0,
        0,
        tmp_value2,
        (tmp_value2**2),
        1.0,
        length=alpha * 1,
        color="#AA0000",
        linewidth=lw,
    )
    ax.quiver(  # 原点を通る直線
        0,
        0,
        0,
        -tmp_value,
        -(tmp_value**2),
        -1.0,
        length=alpha * 1,
        arrow_length_ratio=alr,
        color="#AA0000",
        linewidth=lw,
    )

    ax.view_init(35, 45)

    ax.set(
        xlim=(-L, L),
        ylim=(-L, L),
        zlim=(-L, L),
        xticks=TMP_ARRY,
        yticks=TMP_ARRY,
    )

    ax.set_xlabel("X-axis", fontsize=22)
    ax.set_ylabel("Y-axis", fontsize=22)
    ax.set_zlabel("Z-axis", fontsize=22)
    ax.tick_params(labelsize=18)

    ax.set_title(rf"$ZY=X^2$", fontsize=30, loc="center")
    plt.legend(loc="upper left", borderaxespad=1, fontsize=18)
    plt.close()

    buf = BytesIO()
    fig.savefig(buf)
    return Image.open(buf)


FRAMES = 2
FRAMES = 20 * 3
images = [create_frame(angle) for angle in range(FRAMES)]
images[0].save(
    "./tmp_plane5.gif",
    save_all=True,
    append_images=images[1:],
    duration=100,
    loop=0,
)
