import codecs

import numpy as np
import pandas as pd
from sympy import Eq, solve, symbols

# Duffing 方程式のパラメータ
k = 30
m = 3
c = 5
beta = 3.0
F0 = 100

omega_n = np.sqrt(k / m)  # 共振周波数
zeta = c / (2 * np.sqrt(m * k))
epsilon = beta / m
# epsilon = 0
f0 = F0 / m
print(f"共振周波数: {omega_n=}")
max_freq = 2 * omega_n
step_size = (omega_n - 2) / 30
omega_list = list(np.arange(omega_n - 2, omega_n + 2, step_size))
omega_list = list(np.arange(-10, 10, 0.1))


results = []

for omega in omega_list:
    a = symbols("a")
    equ = Eq(
        ((omega_n**2 - omega**2) * a + (3 / 4) * epsilon * a**3) ** 2
        + (2 * zeta * omega_n * omega * a) ** 2,
        f0**2,
    )
    solutions = solve(equ, a)  # 方程式の解を求める
    # print(f"{omega=}, {solutions=}, {len(solutions)=}***")
    solutions = [
        complex(x).real
        for x in solutions
        if complex(x).real > 0  # 振幅なので正の値のみ採用する
        and np.abs(complex(x).imag) < 0.001  # 虚部が十分小さい場合、実数解とみなす
    ]
    print(f"{omega=}, {solutions=}, {len(solutions)=}***")

    for tmp_ans in solutions:
        print(f"{omega=}, {tmp_ans=}")

        results.append(
            {
                "omega": f"{omega:.9f}",
                "A": tmp_ans,
            }
        )


data_df = pd.DataFrame.from_dict(results, orient="columns")
print(f"{data_df=}")
with codecs.open("./duffing_eq_result.csv", "w", "utf-8_sig", "ignore") as data:
    data_df.to_csv(data, index=False)
