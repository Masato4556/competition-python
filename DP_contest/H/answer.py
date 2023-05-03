
MOD = 10**9+7

H, W = map(int, input().split())
A = [input() for _ in range(H)]

dp = [[0 for _ in range(W)] for _ in range(H)]
dp[0][0] = 1

for h in range(H):
    for w in range(W):
        if A[h][w] == "#":
            continue
        if h > 0:
            dp[h][w] += dp[h-1][w]
        if w > 0:
            dp[h][w] += dp[h][w-1]
        dp[h][w] %= MOD

print(dp[-1][-1])
