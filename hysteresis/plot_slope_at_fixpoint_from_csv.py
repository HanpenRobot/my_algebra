import csv
import seaborn as sns
from io import BytesIO
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image

sns.set(style="darkgrid")

z_label_string = r"$-3{x_e(A,B)}^2-A$"
ans_A = []
ans_B = []
ans_X = []
file_name = "./cube_root_result.csv"
with open(file_name, encoding="UTF-8") as f:
    reader = csv.reader(f)
    num = 0
    for line in reader:
        if num > 0:
            ans_A.append(float(line[0]))
            ans_B.append(float(line[1]))
            ans_X.append(float(line[3]))
        num += 1


def create_frame(angle: int):
    print(f"{angle=}")

    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection="3d")
    sc = ax.scatter(ans_A, ans_B, ans_X, c=ans_X, cmap="viridis", marker="o")
    ax.view_init(30, angle * 4)
    ax.set_xlabel("A-axis", fontsize=22)
    ax.set_ylabel("B-axis", fontsize=22)
    ax.set_zlabel(z_label_string, fontsize=22)

    plt.colorbar(sc)
    plt.close()

    buf = BytesIO()
    fig.savefig(buf)
    return Image.open(buf)


def create_frame2(angle: int):
    print(f"{angle=}")

    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection="3d")
    sc = ax.scatter(ans_A, ans_B, ans_X, c=ans_X, cmap="viridis", marker="o")
    ax.view_init(angle * 4, angle * 4)
    ax.set_xlabel("A-axis", fontsize=22)
    ax.set_ylabel("B-axis", fontsize=22)
    ax.set_zlabel(z_label_string, fontsize=22)

    plt.colorbar(sc)
    plt.close()

    buf = BytesIO()
    fig.savefig(buf)
    return Image.open(buf)


FRAMES = 90
# FRAMES = 180
images = [create_frame(angle) for angle in range(FRAMES)]
images[0].save(
    "./slope_at_fixpoint.gif",
    save_all=True,
    append_images=images[1:],
    duration=100,
    loop=0,
)
