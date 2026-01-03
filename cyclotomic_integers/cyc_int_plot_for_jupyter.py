import numpy as np

# %matplotlib inline
import matplotlib.pyplot as plt
import itertools


def zeta(p, k):
    zeta = np.cos(2 * np.pi / p) + 1j * np.sin(2 * np.pi / p)
    k = k % p
    return zeta**k


def get_zeta_list(zeta, p: int):
    res = []
    for num in range(p):
        tmp_zeta = zeta**num
        res.append(tmp_zeta)
    return res


def get_cyc_num(A: list[int], Zeta: list):
    assert len(A) != Zeta
    res = 0
    for x, y in zip(A, Zeta):
        res += x * y
    return res


def get_norm(arr: list[int], p: int) -> float:
    k = 1
    Z = zeta(p, k)
    zeta_vec = get_zeta_list(zeta=Z, p=p)

    start_value = get_cyc_num(A=arr, Zeta=zeta_vec)

    for k in range(2, p):
        Z = zeta(p, k)
        zeta_vec = get_zeta_list(zeta=Z, p=p)
        res = get_cyc_num(A=arr, Zeta=zeta_vec)
        start_value = start_value * res
    ans = np.abs(start_value)

    return ans


def get_res(arr: list[int], p: int):
    k = 1
    Z = zeta(p, k)
    zeta_vec = get_zeta_list(zeta=Z, p=p)
    cyc_int = get_cyc_num(A=arr, Zeta=zeta_vec)
    start_value = cyc_int

    for k in range(2, p):
        Z = zeta(p, k)
        zeta_vec = get_zeta_list(zeta=Z, p=p)
        res = get_cyc_num(A=arr, Zeta=zeta_vec)
        start_value = start_value * res
    norm = np.abs(start_value)

    return cyc_int, norm


p = 7
L = [-1, 0, 1]
res_norm = []
resX = []
resY = []
norm_res_list = []
for arr in itertools.product(L, repeat=p):
    cyc_int, norm = get_res(arr=arr, p=p)
    res_norm.append(round(norm))
    resX.append(cyc_int.real)
    resY.append(cyc_int.imag)

    # print(f"{res=}************")
print(f"{sorted(list(set(res_norm)))=}***********")
plt.scatter(resX, resY, s=10)
plt.xlabel("X (Real part)")
plt.ylabel("Y (Imag part)")
plt.grid(True)  # Optional: add a grid
plt.rcParams["figure.figsize"] = (10, 10)  # 幅10インチ、高さ10インチ
plt.rcParams["figure.dpi"] = 150  # 150 dpi
plt.show()  # Optional in most modern Jupyter notebooks
