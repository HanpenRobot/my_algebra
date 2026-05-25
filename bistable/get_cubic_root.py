import codecs

import numpy as np
import pandas as pd
from sympy import Eq, solve, symbols

L = 2
R = list(np.arange(-L, L, 0.1))
K = list(np.arange(-L, L, 0.1))

results = []
for r in R:
    for k in K:
        s = symbols("s")
        equ = Eq(r * (1 - (s / k)) - (s / (1 + s**2)), 0)
        solutions = solve(equ, s)  # 3次方程式の解を求める
        solutions = [
            complex(x).real
            for x in solutions
            if np.abs(complex(x).imag) < 0.001  # 虚部が十分小さい場合、実数解とみなす
        ]
        count_sol = len(solutions)
        print(f"{r=}, {k=}, {solutions=}, {count_sol=}")
        for tmp_ans in solutions:
            results.append(
                {
                    "R": r,
                    "K": k,
                    "x": tmp_ans,
                }
            )

data_df = pd.DataFrame.from_dict(results, orient="columns")
print(f"{data_df=}")
with codecs.open("./cubic_root_result.csv", "w", "utf-8_sig", "ignore") as data:
    data_df.to_csv(data, index=False)
