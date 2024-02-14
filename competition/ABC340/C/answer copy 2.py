from math import floor, ceil
N = int(input())

dp = [-1] * (N+1)
dp[0] = 0
for i in range(1, N+1):
    dp[i] = i + dp[floor(i/2)] + dp[ceil(i/2)]

print(dp[-1])
