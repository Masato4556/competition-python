
INF = 10 ** 12
N = int(input())
h = list(map(int, input().split()))


dp = [INF] * N
dp[0] = 0

for i in range(1, N):
    if i == 1:
        dp[i] = dp[i-1] + abs(h[i] - h[i-1])
        continue
    dp[i] = min(dp[i-1] + abs(h[i] - h[i-1]), dp[i-2] + abs(h[i] - h[i-2]))

print(dp[-1])
