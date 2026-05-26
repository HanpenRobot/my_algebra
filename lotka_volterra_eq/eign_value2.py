import numpy as np


def get_jacob_eign_value(a, b, c, d, K1, K2, tmp_vec):

    # print(f"{tmp_vec=}aaaaaaaaaaa")
    jacob_mat = [
        [K1 - 2 * a * tmp_vec[0] - b * tmp_vec[1], -b * tmp_vec[0]],
        [-c * tmp_vec[1], K2 - c * tmp_vec[0] - 2 * d * tmp_vec[1]],
    ]
    # print(f"aaaaaaaaaaaaa{jacob_mat=}")
    e_value, ev = np.linalg.eig(jacob_mat)
    tmp_ans = list(e_value)
    res_list = []
    for i, item in enumerate(tmp_ans):
        res_list.append(rf"$\lambda_{{{i}}}={item:.4f}$")
    return ",".join(res_list)


# a = 2
# b = 1
# c = 1
# d = 3
# K1 = 6
# K2 = 5

# a = 1
# b = 3
# c = 2
# d = 1
# K1 = 5
# K2 = 6

a = 1
b = 3
c = 1
d = 3
K1 = 7.5
K2 = 5

a = 1
b = 3
c = 1
d = 3
K1 = 7.5
K2 = 5

A = [[a, b], [c, d]]
B = [K1, K2]

# det = np.linalg.det(A)

# tmp_vec = np.linalg.solve(A, B)
# res = get_jacob_eign_value(tmp_vec=tmp_vec)
# print(f"{res=}*****")

res = get_jacob_eign_value(tmp_vec=[0, 0])
print(f"{res=}*****")

res = get_jacob_eign_value(tmp_vec=[K1 / a, 0])
print(f"{res=}*****")

res = get_jacob_eign_value(tmp_vec=[0, K2 / d])
print(f"{res=}*****")
