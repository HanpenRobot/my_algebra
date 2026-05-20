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

    x = np.linspace(0, 9, 9)
    y = np.linspace(0, 9, 9)
    X, Y = np.meshgrid(x, y)
    ax.plot_surface(X, Y, Z=X * 0 + 5.0, color="g", alpha=0.6)

    ax.plot_surface(X, Y=X * 0 + 5.0, Z=Y, color="y", alpha=0.6)

    ax.plot_surface(X=X * 0 + 5.0, Y=Y, Z=X, color="r", alpha=0.6)

    # ax.view_init(30, angle * 4)
    ax.view_init(angle * 2, angle * 2)
    ax.set(
        xlim=(0, 9),
        ylim=(0, 9),
        zlim=(0, 9),
        xticks=np.arange(0, 10, 2),
        yticks=np.arange(0, 10, 1),
        zticks=np.arange(0, 10, 1),
    )

    ax.set_xlabel("X-axis", fontsize=22)
    ax.set_ylabel("Y-axis", fontsize=22)
    ax.set_zlabel("Z-axis", fontsize=22)
    ax.tick_params(labelsize=22)
    ax.set_title(rf"view_init({angle*2:.2f}, {angle*2:.2f})", fontsize=30, loc="center")
    plt.close()

    buf = BytesIO()
    fig.savefig(buf)
    return Image.open(buf)


FRAMES = 2
FRAMES = 180
images = [create_frame(angle) for angle in range(FRAMES)]
images[0].save(
    "./tmp_plane.gif",
    save_all=True,
    append_images=images[1:],
    duration=100,
    loop=0,
)
