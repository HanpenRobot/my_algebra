import codecs

import numpy as np
import pandas as pd


def henon_map(x: float, y: float):

    a = 1.063
    b = 0.3

    N = 1000

    x1 = x
    y1 = y
    ans_list = []
    for num in range(N):
        x2 = y1 + 1.0 - a * x1 * x1
        y2 = b * x1
        x1 = x2
        y1 = y2
        if num > N * 0.9:
            if np.abs(x2) > 1000.0 or np.abs(y2) > 1000.0:
                return []
            ans_list.append((x2, y2))
    return list(set(ans_list))


L = 1.5
A = list(np.arange(-L, L, 0.005))
B = list(np.arange(-L, L, 0.005))

results = []
for a in A:
    for b in B:
        res = henon_map(a, b)
        len_res = len(res)
        # if len_res != 0 and len_res == 6:
        if len_res < 50 or len_res == 0:
            # print(f"{a=}, {b=}, {len_res=}")
            results.append({"x": a, "y": b, "ans_len": len_res})


data_df = pd.DataFrame.from_dict(results, orient="columns")
print(f"{data_df=}")
with codecs.open("./ans_henon_map_init2.csv", "w", "utf-8_sig", "ignore") as data:
    data_df.to_csv(data, index=False)
