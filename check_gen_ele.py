def check_gen_ele(q: int, N: int) -> int:
    """qがZ/N*Zの生成元であるか確認する関数"""
    # q = 54  # Z/N*Zの生成元
    # N = 61
    res = []
    for num in range(1, N):
        ans = q**num % N
        # print(f"{num=},{ans=}****")
        res.append(ans)

    print(f"{q=}*******,{set(res)=}***")

    # assert set(res) == set(range(1, N)), f"{q=}はZ/{N}*Zの生成元ではない!"
    if set(res) == set(range(1, N)):
        print(f"{q=}はZ/{N}*Zの生成元である。")
        return q
    else:
        # print(f"{q=}はZ/{N}*Zの生成元ではない!")
        return -1


# gen_list = [6, 7, 44, 59, 31, 18, 26, 10, 55, 54, 17, 2, 30, 43, 35, 51]
# N = 61
N = 13
gen_list = range(2, N)

print(f"{len(gen_list)=}*****")
for q in gen_list:
    # print(f"{q=}")
    res = check_gen_ele(q=q, N=N)
    # print(f"{res=}****")
