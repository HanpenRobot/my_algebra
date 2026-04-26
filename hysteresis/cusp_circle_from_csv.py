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
file_name = "./cube_root_result.csv"
with open(file_name, encoding="UTF-8") as f:
    reader = csv.reader(f)
    num = 0
    for line in reader:
        if num > 0 and float(line[3]) < 0:  # 安定不動点のみをプロットする
            ans_A.append(float(line[0]))
            ans_B.append(float(line[1]))
            ans_X.append(float(line[2]))
        num += 1

ans_A2 = []
ans_B2 = []
ans_X2 = []
ans_C2 = []
file_name = "./ans_dump_circle002.csv"
with open(file_name, encoding="UTF-8") as f:
    reader = csv.reader(f)
    num = 0
    for line in reader:
        if num > 0:
            ans_A2.append(float(line[0]))
            ans_B2.append(float(line[1]))
            ans_X2.append(-float(line[3]))
            ans_C2.append(float(10.0))
        num += 1


def create_frame(angle: int):
    print(f"{angle=}")

    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection="3d")
    sc = ax.scatter(ans_A, ans_B, ans_X, c=ans_X, cmap="viridis", marker="o")
    ax.view_init(30, angle * 4)
    ax.set_xlabel("A-axis", fontsize=22)
    ax.set_ylabel("B-axis", fontsize=22)
    ax.set_zlabel("x-axis", fontsize=22)

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
    ax.view_init(-90, -90)
    ax.set_xlabel("A-axis", fontsize=22)
    ax.set_ylabel("B-axis", fontsize=22)
    # ax.set_zlabel("x-axis", fontsize=22)

    plt.colorbar(sc)
    plt.close()

    buf = BytesIO()
    fig.savefig(buf)
    return Image.open(buf)


def create_frame3(angle: int):
    print(f"{angle=}")

    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection="3d")
    sc = ax.scatter(ans_A, ans_B, ans_X, c=ans_X, cmap="viridis", marker="o")
    sc = ax.scatter(ans_A2, ans_B2, ans_X2, c="r", marker="o")
    # ax.view_init(-90, -90)
    # ax.view_init(60, 180)
    ax.view_init(angle * 4, angle * 4)
    # ax.view_init(30, angle * 4)

    ax.set_xlabel("A-axis", fontsize=22)
    ax.set_ylabel("B-axis", fontsize=22)
    ax.set_zlabel("x-axis", fontsize=22)

    # plt.colorbar(sc)
    plt.close()

    buf = BytesIO()
    fig.savefig(buf)
    return Image.open(buf)


def create_frame4(angle: int):
    print(f"{angle=}")

    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection="3d")
    sc = ax.scatter(ans_A, ans_B, ans_X, c=ans_X, cmap="viridis", marker="o")
    sc = ax.scatter(ans_A2, ans_B2, ans_X2, c="r", marker="o")
    # ax.view_init(-90, -90)
    # ax.view_init(60, 180)
    # ax.view_init(angle * 4, angle * 4)
    ax.view_init(30, angle * 4)

    ax.set_xlabel("A-axis", fontsize=22)
    ax.set_ylabel("B-axis", fontsize=22)
    ax.set_zlabel("x-axis", fontsize=22)

    # plt.colorbar(sc)
    plt.close()

    buf = BytesIO()
    fig.savefig(buf)
    return Image.open(buf)


def create_frame5(angle: int):
    print(f"{angle=}")

    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection="3d")
    sc = ax.scatter(ans_A, ans_B, ans_X, c=ans_X, cmap="viridis", marker="o")
    step_size = int(len(ans_X2) * angle / 30)
    sc = ax.scatter(
        ans_A2[:step_size], ans_B2[:step_size], ans_X2[:step_size], c="r", marker="o"
    )
    # ax.view_init(-90, -90)
    # ax.view_init(60, 180)
    # ax.view_init(angle * 4, angle * 4)
    ax.view_init(45, -145)

    ax.set_xlabel("A-axis", fontsize=22)
    ax.set_ylabel("B-axis", fontsize=22)
    ax.set_zlabel("x-axis", fontsize=22)

    # plt.colorbar(sc)
    plt.close()

    buf = BytesIO()
    fig.savefig(buf)
    return Image.open(buf)


FRAMES = 1
# FRAMES = 180
FRAMES = 1
FRAMES = 180
param_size = len(ans_X2)
FRAMES = int(param_size / 30)
images = [create_frame5(angle) for angle in range(FRAMES)]
images[0].save(
    "./circle_runge_kutta_final2c.gif",
    save_all=True,
    append_images=images[1:],
    duration=100,
    loop=0,
)
