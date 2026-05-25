import codecs

import numpy as np
import pandas as pd
from sympy import Eq, solve, symbols

L = 0.05
L2 = 6
# R = list(np.arange(0, 0.8, 0.01))
# K = list(np.arange(4, 6, 0.01))
R = list(np.arange(0.5, 0.9, 0.01))
K = list(np.arange(4, 9, 0.01))

# r=3*sqrt(3)/8=0.649
# k=3*sqrt(3)=5.19

# r * (1 - (s / k)) = (s / (1 + s**2))
# r * (1 - (s / k)) (1 + s**2) = s
# r*(1/s-(1/k)) (1+s**2) = 1
import numpy as np

# 係数リスト: [x^3の係数, x^2の係数, xの係数, 定数項]
# coeffs = [1, 0, -1, 0]

# roots = np.roots(coeffs)
# print(roots)


# r - s - (r s)/k + r s^2 - (r s^3)/k

results = []
for r in R:
    for k in K:
        # s = symbols("s")
        # equ = Eq(r * (1 - (s / k)) - (s / (1 + s**2)), 0)
        # solutions = solve(equ, s)  # 3次方程式の解を求める
        coeffs = [-r / k, r, -(1 + r / k), r]

        try:
            solutions = np.roots(coeffs)
        except:
            print(f"Err: {coeffs=}")
            continue
        # print(f"############{solutions=}")
        solutions = [
            complex(x).real
            for x in solutions
            if np.abs(complex(x).imag) < 0.001  # 虚部が十分小さい場合、実数解とみなす
        ]
        count_sol = len(solutions)
        # print(f"{r=}, {k=}, {solutions=}, {count_sol=}")
        if count_sol != 1:
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
