import csv
import seaborn as sns
from io import BytesIO
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image

sns.set(style="darkgrid")


ans_A = []
ans_B = []
ans_X = []
file_name = "./cubic_root_result.csv"
with open(file_name, encoding="UTF-8") as f:
    reader = csv.reader(f)
    num = 0
    for line in reader:
        if num > 0:
            ans_A.append(float(line[0]))
            ans_B.append(float(line[1]))
            ans_X.append(float(line[2]))
        num += 1


def create_frame(angle: int):
    print(f"{angle=}")

    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection="3d")
    sc = ax.scatter(ans_A, ans_B, ans_X, c=ans_X, cmap="viridis", marker="o")
    ax.view_init(angle * 8, angle * 8)
    ax.set_xlabel("R-axis", fontsize=22)
    ax.set_ylabel("K-axis", fontsize=22)
    ax.set_zlabel("n-axis", fontsize=22)

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
    ax.set_xlabel("R-axis", fontsize=22)
    ax.set_ylabel("K-axis", fontsize=22)
    ax.set_zlabel("n-axis", fontsize=22)

    plt.colorbar(sc)
    plt.close()

    buf = BytesIO()
    fig.savefig(buf)
    return Image.open(buf)


FRAMES = 45
FRAMES = 90
images = [create_frame2(angle) for angle in range(FRAMES)]
images[0].save(
    "./output001.gif",
    save_all=True,
    append_images=images[1:],
    duration=100,
    loop=0,
)
