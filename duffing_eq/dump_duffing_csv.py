import codecs

import numpy as np
import pandas as pd
from sympy import Eq, solve, symbols

# Duffing 方程式のパラメータ
k = 500
m = 3
c = 6
beta = 5
F0 = 30

omega_n = np.sqrt(k / m)  # 共振周波数
zeta = c / (2 * np.sqrt(m * k))
# epsilon = beta / m
epsilon = 0
f0 = F0 / m
print(f"共振周波数: {omega_n=}")
max_freq = 2 * omega_n
step_size = max_freq / 100
omega_list = list(np.arange(-max_freq, max_freq, step_size))

results = []

for omega in omega_list:
    a = symbols("a")
    equ = Eq(
        ((omega_n**2 - omega**2) * a) ** 2 + (2 * zeta * omega_n * omega * a) ** 2,
        f0**2,
    )
    solutions = solve(equ, a)  # 方程式の解を求める
    solutions = [
        complex(x).real
        for x in solutions
        if complex(x).real > 0  # 振幅なので正の値のみ採用する
        and np.abs(complex(x).imag) < 0.001  # 虚部が十分小さい場合、実数解とみなす
    ]
    for tmp_ans in solutions:
        print(f"{omega=}, {tmp_ans=}")

        results.append(
            {
                "omega": omega,
                "A": tmp_ans,
            }
        )


data_df = pd.DataFrame.from_dict(results, orient="columns")
print(f"{data_df=}")
with codecs.open("./duffing_eq_result.csv", "w", "utf-8_sig", "ignore") as data:
    data_df.to_csv(data, index=False)
