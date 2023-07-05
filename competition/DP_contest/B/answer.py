INF = 10 ** 12

n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = [INF] * n
dp[0] = 0

for i in range(1, n):
    for j in range(1, k+1):
        if i-j < 0: continue
        dp[i] = min(dp[i], dp[i-j] + abs(h[i] - h[i-j]))

print(dp[-1])