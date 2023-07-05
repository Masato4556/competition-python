# テストデータ生成など、回答とは関係のないコードを実行するファイル

'''
A 個が XX
B 個が XY
C 個が YX
D 個が YY
'''

from random import randint

N = 8

ans = set()


for testcase in range(2**N):

    S = [""] * N
    for i in range(N):
        S[i] = "Y" if (1 << i) & testcase else "X"

    counter = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        }

    for i in range(N-1):
        isx_ = True if S[i] == "X" else False
        is_x = True if S[i+1] == "X" else False

        if isx_:
            if is_x:
                counter["A"] += 1
            else:
                counter["B"] += 1
        else:
            if is_x:
                counter["C"] += 1
            else:
                counter["D"] += 1

    ans.add((counter["A"], counter["B"], counter["C"], counter["D"]))

ans_list = list(ans)
ans_list.sort()
for a in ans_list:
    print(a)


all_case = set()
for i in range(0, N-1):
    for j in range(0, N-1-i):
        for k in range(0, N-1-i-j):
            all_case.add((i, j, k, N-1-i-j-k))
                

print("No testcase")
for a in all_case - ans:
    print(a)