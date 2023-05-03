# dpに重さを含めると、状態数が多くなりすぎる

from collections import defaultdict
N, W = map(int, input().split())

dp = [defaultdict(int) for _ in range(N+1)]
dp[0][0] = 0

for i in range(1, N+1):
    w, v = map(int, input().split())
    for p_w in dp[i-1].keys():
        dp[i][p_w] = max(dp[i][p_w], dp[i-1][p_w])
        if p_w + w > W: continue
        dp[i][p_w+w] = max(dp[i][p_w+w], dp[i-1][p_w] + v)

print(max([v for v in dp[-1].values()]))
