import csv
import seaborn as sns
from io import BytesIO
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image

sns.set(style="darkgrid")

FRAMES = 180

ans_X = []
ans_Y = []
ans_Z = []
file_name = "./ans_lorentz.csv"
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
    step_size = len(ans_Z) / FRAMES
    pos = int(step_size * angle)
    sc = ax.scatter(
        ans_X[:pos], ans_Y[:pos], ans_Z[:pos], c=ans_Z[:pos], cmap="viridis", marker="o"
    )
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


images = [create_frame(angle) for angle in range(FRAMES)]
images[0].save(
    "./lorentz_plot_anim.gif",
    save_all=True,
    append_images=images[1:],
    duration=100,
    loop=0,
)
