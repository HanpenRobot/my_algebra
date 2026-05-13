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

n = 50
x0 = 0.10001
x1 = 0.1

x = x1
X = []
Y = []
Y2 = []
for k in range(n):
    X.append(k)
    x = 4.0 * x * (1.0 - x)
    Y.append(x)
    Y2.append(np.sin((2.0 ** (k + 1)) * np.arcsin(np.sqrt(x0))) ** 2)
GRID_COLOR = "#444444"
GRID_LINE_WIDTH = 0.8
plt.ylim(-0.5, 1.5)
plt.plot(X, Y2, "-o", label=r"Exact solution (init. $x_0$=%.1f)" % x1)
plt.plot(X, Y, "-v", label=r"Numerical solution (init.  $x_0$=%.5f)" % x0)
plt.legend()
plt.grid(which="both", color=GRID_COLOR, linestyle="--", linewidth=GRID_LINE_WIDTH)
plt.xlabel(r"$n$")
plt.ylabel(r"$x_{n}$")
plt.rcParams["font.size"] = 23

# plt.show()
plt.savefig("logistic_exact_vs_numerical.png")
