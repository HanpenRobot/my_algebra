import csv
import seaborn as sns
from io import BytesIO
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
from matplotlib.animation import FuncAnimation
import numpy as np

# sns.set(style="darkgrid")

fig = plt.figure(dpi=256)

n = 10000
x0 = 0.1
x = x0
X = []
Y = []
for k in range(n):
    X.append(k)
    x = 4.0 * x * (1.0 - x)
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
plt.ylim(0, 0.07)
ax.set_xlabel(r"$x_{n}$", fontsize=18)
ax.set_ylabel(r"$\rho(x)$", fontsize=18)
plt.savefig("logistic_invariant_dist.png")
