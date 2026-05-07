import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import math
import csv

FRAMES = 180
fig = plt.figure(dpi=256)
ans_X = []
ans_Y = []

file_name = "./julia_dump2.csv"
with open(file_name, encoding="UTF-8") as f:
    reader = csv.reader(f)
    num = 0
    for line in reader:
        if num > 0:
            ans_X.append(float(line[0]))
            ans_Y.append(float(line[1]))
        num += 1
L = 2.0
limit_const = 0.7
CURVE_LINE_COLOR = "#0000FF"
RT_LINE_COLOR = "#FF0000"
XY_LINE_COLOR = "#00AA00"
X_AXIS_LINE_COLOR = "#000000"
Y_AXIS_LINE_COLOR = "#000000"
GRID_COLOR = "#444444"

LINE_WIDTH = 1
AXIS_LINE_WIDTH = 0.8
GRID_LINE_WIDTH = 0.8

FIGURE_SIZE = (10, 10)
Y_AXIS_MAX = 3.5
Y_AXIS_MIN = -3.5
X_AXIS_MAX = 3.0
X_AXIS_MIN = -3.0

TITLE_FONT_SIZE = 14
LABEL_FONT_SIZE = 16
TAIL = 1.0
# plt.cla()
# 縦横比を1:1に設定

plt.axes().set_aspect("equal")
plt.xlabel(r"real part", fontsize=LABEL_FONT_SIZE)
plt.ylabel(r"image part", fontsize=LABEL_FONT_SIZE)
plt.grid(which="both", color=GRID_COLOR, linestyle="--", linewidth=GRID_LINE_WIDTH)
x_grid_list = np.arange(X_AXIS_MIN, X_AXIS_MAX + TAIL, TAIL)
plt.xticks(x_grid_list)
y_grid_list = np.arange(Y_AXIS_MIN, Y_AXIS_MAX + TAIL, TAIL)
plt.yticks(y_grid_list)

plt.xlim(X_AXIS_MIN, X_AXIS_MAX)
plt.ylim(Y_AXIS_MIN, Y_AXIS_MAX)

plt.plot(ans_X, ans_Y, "s", ms=1.0, color=RT_LINE_COLOR)

plt.savefig("complex_ans001b.png")
