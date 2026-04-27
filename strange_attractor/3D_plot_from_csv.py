import csv
import seaborn as sns
from io import BytesIO
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image

sns.set(style="darkgrid")


ans_X = []
ans_Y = []
ans_Z = []
file_name = "./ans_piecewise_linear.csv"
with open(file_name, encoding="UTF-8") as f:
    reader = csv.reader(f)
    num = 0
    for line in reader:
        if num > 0 and num % 50 == 0:
            ans_X.append(float(line[1]))
            ans_Y.append(float(line[2]))
            ans_Z.append(float(line[3]))
        num += 1


def create_frame(angle: int):
    print(f"{angle=}")

    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection="3d")
    sc = ax.scatter(ans_X, ans_Y, ans_Z, c=ans_Z, cmap="viridis", marker="o")
    # ax.view_init(30, angle * 4)
    ax.view_init(angle * 2, angle * 2)
    ax.set_xlabel("X-axis", fontsize=22)
    ax.set_ylabel("Y-axis", fontsize=22)
    ax.set_zlabel("Z-axis", fontsize=22)

    plt.colorbar(sc)
    plt.close()

    buf = BytesIO()
    fig.savefig(buf)
    return Image.open(buf)


# def create_frame2(angle: int):
#     print(f"{angle=}")

#     fig = plt.figure(figsize=(12, 12))
#     ax = fig.add_subplot(111, projection="3d")
#     sc = ax.scatter(ans_A, ans_B, ans_X, c=ans_X, cmap="viridis", marker="o")
#     ax.view_init(angle * 2, angle * 2)
#     ax.set_xlabel("A-axis", fontsize=22)
#     ax.set_ylabel("B-axis", fontsize=22)
#     ax.set_zlabel("x-axis", fontsize=22)

#     plt.colorbar(sc)
#     plt.close()

#     buf = BytesIO()
#     fig.savefig(buf)
#     return Image.open(buf)


FRAMES = 90
FRAMES = 180
FRAMES = 180
images = [create_frame(angle) for angle in range(FRAMES)]
images[0].save(
    "./piecewise_linear.gif",
    save_all=True,
    append_images=images[1:],
    duration=100,
    loop=0,
)
