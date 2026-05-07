import csv
import seaborn as sns
from io import BytesIO
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
from matplotlib.animation import FuncAnimation
import numpy as np
import math
import codecs

import numpy as np
import pandas as pd

sns.set(style="darkgrid")

FRAMES = 180
fig = plt.figure(dpi=256)


def func(z: complex):
    a = 3.3
    return a * z * (1.0 - z)


def check_func(z: complex) -> bool:
    TRY_NUM = 10
    epsilon = 1000.0  # 発散したかどうかのしきい値
    for num in range(TRY_NUM):

        z = func(z)
        tmp_abs = np.abs(z)
        if math.isnan(z.real):
            # 写像を計算した結果、発散したらFalseを返却する
            return False
        if tmp_abs > epsilon:
            # 写像した結果の絶対値がしきい値を超えたら、発散と判定しFalseを返却する
            return False
    return True


L = 4
A = list(np.arange(-L, L, 0.01))
B = list(np.arange(-L, L, 0.01))

results = []
for a in A:
    for b in B:

        ans = check_func(complex(a, b))
        print(f"{a=}, {b=}, {ans=}")
        if ans is True:

            results.append(
                {
                    "A": f"{a:.10f}",
                    "B": f"{b:.10f}",
                }
            )

data_df = pd.DataFrame.from_dict(results, orient="columns")
print(f"{data_df=}")
with codecs.open("./julia_dump.csv", "w", "utf-8_sig", "ignore") as data:
    data_df.to_csv(data, index=False)
