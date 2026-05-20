import codecs

import numpy as np
import pandas as pd
from tqdm import tqdm


def henon_map(a: float, x: float, y: float):

    # a = 1.063
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
X = list(np.arange(-L, L, 0.005))
Y = list(np.arange(-L, L, 0.005))
A = list(np.arange(1.000, 1.4, 0.01))


results = []
num = 0
for a in tqdm(A):
    for x in X:
        for y in Y:
            res = henon_map(a, x, y)
            len_res = len(res)
            # if len_res != 0 and len_res == 6:
            if len_res < 50 or len_res == 0:
                # print(f"{a=}, {b=}, {len_res=}")
                results.append({"num": num, "a": a, "x": x, "y": y, "ans_len": len_res})
    num += 1


data_df = pd.DataFrame.from_dict(results, orient="columns")
print(f"{data_df=}")
with codecs.open("./ans_henon_map_init4.csv", "w", "utf-8_sig", "ignore") as data:
    data_df.to_csv(data, index=False)
