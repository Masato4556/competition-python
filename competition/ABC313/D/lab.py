# テストデータ生成など、回答とは関係のないコードを実行するファイル

K = 3
A = [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1]
N = len(A)
T = []

A_e = [-1] * 0

for i in range(len(A)):
    v = 0
    for j in range(K):
        v += A[(i+j) % len(A)]
    T.append(v % 2)
    print(i, i+K-1,  "|", v % 2)


# print("=======")
# print(sum(T))

G = [set() for _ in range(N)]

A_e = [99] * N

v = 0

G = [99] * N

for i in range(N):
    if T[i] == T[(i+1) % N]:
        if A_e[i] == 99 and A_e[(i+K) % N] == 99:
            A_e[i] = v
            A_e[(i+K) % N] = v
            v += 1
        else:
            A_e[i] = min(A_e[i], A_e[(i+K) % N])
            A_e[(i+K) % N] = min(A_e[i], A_e[(i+K) % N])
    else:
        if A_e[i] == 99 and A_e[(i+K) % N] == 99:
            A_e[i] = v
            v += 1
            A_e[(i+K) % N] = v
        else:
            A_e[i] = min(A_e[i], A_e[(i+K) % N])
            A_e[(i+K) % N] = min(A_e[i], A_e[(i+K) % N]) + 1

print(A_e)
