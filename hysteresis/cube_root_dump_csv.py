import codecs

import numpy as np
import pandas as pd
from sympy import Eq, solve, symbols


def func(x: float, a: float):
    return -3 * x ^ 2 + a


L = 30
A = list(np.arange(-L, L, 1))
B = list(np.arange(-L, L, 1))

results = []
for a in A:
    for b in B:
        s = symbols("s")
        equ = Eq(-(s**3) + a * s + b, 0)
        solutions = solve(equ, s)  # 3次方程式の解を求める
        solutions = [
            complex(x).real
            for x in solutions
            if np.abs(complex(x).imag) < 0.001  # 虚部が十分小さい場合、実数解とみなす
        ]
        count_sol = len(solutions)
        print(f"{a=}, {b=}, {solutions=}, {count_sol=}")
        for tmp_ans in solutions:
            tmp_x = func(x=tmp_ans, a=a)
            results.append(
                {
                    "A": a,
                    "B": b,
                    "x_e": tmp_ans,
                    "-3(x_e)^2": tmp_x,
                    "count_sol": count_sol,
                }
            )

data_df = pd.DataFrame.from_dict(results, orient="columns")
print(f"{data_df=}")
with codecs.open("./cube_root_result.csv", "w", "utf-8_sig", "ignore") as data:
    data_df.to_csv(data, index=False)
