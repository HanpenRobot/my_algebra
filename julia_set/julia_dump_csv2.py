import csv
import numpy as np
import math
import codecs

import pandas as pd


def func(z: complex):
    return z * z - 1.0


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
step_size = 0.005
A = list(np.arange(-L, L, step_size))
B = list(np.arange(-L, L, step_size))

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
with codecs.open("./julia_dump2.csv", "w", "utf-8_sig", "ignore") as data:
    data_df.to_csv(data, index=False)
