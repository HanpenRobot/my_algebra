import numpy as np


def get_eign_value(A, B):
    det = np.linalg.det(A)
    if det == 0:
        return None
    # print(f"{det=}****")

    tmp_sol = np.linalg.solve(A, B)
    # print(f"{tmp_sol=}")
    jacob_mat = [
        [K1 - 2 * a * tmp_sol[0] - b * tmp_sol[1], -b * tmp_sol[0]],
        [-c * tmp_sol[1], K2 - c * tmp_sol[0] - 2 * d * tmp_sol[1]],
    ]
    e_value, ev = np.linalg.eig(jacob_mat)
    return list(e_value)
    # print(f"{e_value=}****")


# a = 2
# b = 1
# c = 1
# d = 3
# K1 = 6
# K2 = 5

a = 1
b = 3
c = 2
d = 1
K1 = 5
K2 = 6
res = get_eign_value(A=[[a, b], [c, d]], B=[K1, K2])
print(f"{res=}*****")
