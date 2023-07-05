INF = 10 ** 12
from collections import defaultdict
N, W = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
dp = [defaultdict(lambda: INF) for _ in range(N+1)]
dp[0][0] = 0

for i in range(1, N+1):
    w, v = items[i-1]
    for p_v, p_w in dp[i-1].items():
        # 重くないほうがより多くのものを詰められるので、重さはより軽い方を選択する
        dp[i][p_v] = min(dp[i][p_v], p_w)
        dp[i][p_v+v] = min(dp[i][p_v+v], p_w + w)

print(max([v for v, w in dp[-1].items() if w <= W]))
