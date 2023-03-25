from itertools import permutations

# 到達可能か

    # 再帰的に探索する関数


n, m = map(int, input().split())
S = []
sum_S_len = 0
X_min, X_max = 3, 16
for _ in range(n):
    S.append(input())


T = set()
for _ in range(m):
    T.add(input())

def dfs(x, inds, i):
    if i == n:
        if x not in T and 3 <= len(x) <= 16:
            print(x)
            exit()
        return
    for j in range(1, 16-len(x)):
        dfs(x + "_"*j + S[inds[i]], inds, i+1)

for inds in permutations(range(n)):
    dfs(S[inds[0]], inds, 1)

print(-1)