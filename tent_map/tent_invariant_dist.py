import csv
import seaborn as sns
from io import BytesIO
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
from matplotlib.animation import FuncAnimation
import numpy as np

fig = plt.figure(dpi=256)


def func(x: float) -> float:
    """テント写像の値を求める"""
    # alpha = 2
    # if 0 <= x and x <= 0.5:
    #     return alpha * x
    # else:
    #     return -alpha * x + alpha

    if x <= 0.5:
        return 2 * x
    else:
        return 1.99999999 * (1 - x)


n = 10**6
x0 = 0.1
x = x0
X = []
Y = []
for k in range(n):
    X.append(k)
    x = func(x)
    Y.append(x)
print(X)
print(Y)
weights = np.ones_like(Y) / float(len(Y))
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.hist(Y, bins=100, weights=weights)
GRID_COLOR = "#444444"
GRID_LINE_WIDTH = 0.8
plt.grid(which="both", color=GRID_COLOR, linestyle="--", linewidth=GRID_LINE_WIDTH)

ax.set_aspect("auto")
plt.xlim(0, 1)
plt.ylim(0, 0.025)
ax.set_title(r"Invariant measure $\rho(x)$ ($n=10^6$)")
ax.set_xlabel(r"$x_{n}$", fontsize=18)
ax.set_ylabel(r"$\rho(x)$", fontsize=18)
plt.savefig("tent_invariant_dist.png")
