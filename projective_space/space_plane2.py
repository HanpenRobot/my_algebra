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
    ax.plot_surface(X, Y, Z=X * 0 + 1.0, color="#00AA00", alpha=0.3)
    ax.plot_surface(X, Y=X * 0 + 1.0, Z=Y, color="y", alpha=0.3)

    ax.plot_surface(X=X * 0 + 1.0, Y=Y, Z=X, color="r", alpha=0.3)

    # ax.plot_surface(X, Y, Z=X * 0, color="#0000FF", alpha=0.4)

    # 矢幅・矢長比・矢頭長比を指定
    lw = 3
    l = 1.0
    alr = 0.1
    # ax.quiver(0, 0, 3, 4, angles="xy", scale_units="xy", scale=1, color="blue")
    ax.quiver(  # Z軸の矢印
        0,
        0,
        0,
        0,
        0,
        4,
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
        3,
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
        3,
        0,
        0,
        length=l,
        arrow_length_ratio=alr,
        color="#000000",
        linewidth=lw,
    )

    TMP_ARRY2 = np.linspace(-L, L, 20 * L + 1)
    # 放物線の値を生成
    graph_x = TMP_ARRY2
    graph_y = TMP_ARRY2**2
    graph_z = TMP_ARRY2 * 0 + 1.0
    # num = 14
    num = angle

    alpha = 2.0
    ax.quiver(  # 原点を通る直線
        0,
        0,
        0,
        graph_x[num],
        graph_y[num],
        graph_z[num],
        length=alpha * 1,
        arrow_length_ratio=alr,
        color="#AA0000",
        linewidth=lw,
    )
    ax.quiver(  # Z軸の矢印
        0,
        0,
        0,
        -graph_x[num],
        -graph_y[num],
        -graph_z[num],
        length=alpha * 1,
        arrow_length_ratio=alr,
        color="#AA0000",
        linewidth=lw,
    )

    # sc = ax.scatter(graph_x, graph_y, graph_z, c=graph_z, cmap="viridis", marker="o")
    # plt.colorbar(sc)
    sc = ax.plot(graph_x, graph_y, graph_z, c="#FF0000", marker="o")
    # sc = ax.scatter(graph_x, graph_y, graph_z, c="r", marker="o")
    # plt.colorbar(sc)
    # sc = ax.scatter(
    #     ans_X[:pos], ans_Y[:pos], ans_Z[:pos], c=ans_Z[:pos], cmap="viridis", marker="o"
    # )
    # >>> np.linspace(-9, 9, 19)
    # array([-9., -8., -7., -6., -5., -4., -3., -2., -1.,  0.,  1.,  2.,  3.,
    #         4.,  5.,  6.,  7.,  8.,  9.])

    # array([0.   , 1.125, 2.25 , 3.375, 4.5  , 5.625, 6.75 , 7.875, 9.   ])
    # >>> len(np.linspace(0, 9, 9))
    # 9
    # ax.plot_surface(X, Y=X * 0 + 5.0, Z=Y, color="y", alpha=0.6)

    # ax.plot_surface(X=X * 0 + 5.0, Y=Y, Z=X, color="r", alpha=0.6)

    # ax.view_init(30, angle * 4)
    # ax.view_init(angle * 2, angle * 2)
    ax.view_init(30, 40)

    ax.set(
        xlim=(-L, L),
        ylim=(-L, L),
        zlim=(0, 5.0),
        xticks=TMP_ARRY,
        yticks=TMP_ARRY,
        # zticks=np.linspace(0, 2 * L, 2 * L + 1),
    )

    ax.set_xlabel("X-axis", fontsize=22)
    ax.set_ylabel("Y-axis", fontsize=22)
    ax.set_zlabel("Z-axis", fontsize=22)
    ax.tick_params(labelsize=22)
    # ax.set_title(rf"view_init({angle*2:.2f}, {angle*2:.2f})", fontsize=30, loc="center")
    plt.close()

    buf = BytesIO()
    fig.savefig(buf)
    return Image.open(buf)


FRAMES = 2
# FRAMES = 180

FRAMES = 20 * 3 - 3
images = [create_frame(angle) for angle in range(FRAMES)]
images[0].save(
    "./tmp_plane2.gif",
    save_all=True,
    append_images=images[1:],
    duration=100,
    loop=0,
)
