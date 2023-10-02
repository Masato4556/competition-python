from collections import defaultdict
INF = 10**16

N = 6
A = [
    # value, cost
    (1, 5),
    (2, 4),
    (3, 1),
    (4, 2),
    (5, 6),
    (6, 2),
]


# dpの初期化
#
# dp[n][v] = c
# Anまでを用いて、vの値を作るために必要な最小コストc
dp = [defaultdict(lambda: INF) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    v, c = A[i]
    dp_cp = dp[i].copy()
    for key in dp_cp.keys():
        dp[i+1][key] = min(dp[i+1][key], dp[i][key])
        dp[i+1][key+v] = min(dp[i+1][key+v], dp[i][key] + c)


print(dp[i+1][7])
