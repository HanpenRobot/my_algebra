import csv
import seaborn as sns
from io import BytesIO
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
from matplotlib.animation import FuncAnimation
import numpy as np

sns.set(style="darkgrid")

fig = plt.figure(dpi=256)
N = 5000
X = []
Y2 = []
Y3 = []
for n in range(500, N, 100):
    x1 = 0.1
    x = x1
    Y = []
    for k in range(0, n, 1):
        x = 4.0 * x * (1.0 - x)
        Y.append(np.log(np.fabs(4.0 * (1.0 - 2.0 * x))))

    ave = sum(Y) / len(Y)
    print(ave)
    X.append(n)
    Y2.append(ave)
    Y3.append(np.log(2))
print(X)
print(Y2)
plt.plot(X, Y2, "-o", linewidth=2, label="Numerical solution", color="#0000FF")
plt.plot(X, Y3, "--", linewidth=2, label="log(2)", color="#00AA00")
ans = Y2.pop()
print(ans)
e = np.fabs((np.log(2) - ans) / np.log(2)) * 100
print("Relative error=%f" % e)
plt.legend()
plt.ylim(0.69, 0.695)

GRID_COLOR = "#444444"
GRID_LINE_WIDTH = 0.8
plt.grid(which="both", color=GRID_COLOR, linestyle="--", linewidth=GRID_LINE_WIDTH)


plt.xlabel(r"$n$")
plt.ylabel(r"Lyapunov exponent $\lambda$")
plt.rcParams["font.size"] = 33

plt.savefig("lyapunov_plot.png")
