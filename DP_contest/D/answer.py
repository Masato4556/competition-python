

N, W = map(int, input().split())

dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
for i in range(1, N+1):
    w, v = map(int, input().split())
    for j in range(W+1):
        dp[i][j] = dp[i-1][j]
        if j-w < 0: continue
        dp[i][j] = max(dp[i][j], dp[i-1][j-w] + v)

print(max(dp[-1]))
