X, Y, Z = map(int, input().split())
S = input()
N = len(S)

dp = [[0] * 2 for _ in range(N+1)]
dp[0][1] = Z
for i in range(N):
    if S[i] == "a":
        dp[i+1][0] = min(dp[i][0] + X, dp[i][1] + X + Z)
        dp[i+1][1] = min(dp[i][1] + Y, dp[i][0] + Y + Z)
    else:
        dp[i+1][0] = min(dp[i][0] + Y, dp[i][1] + Y + Z)
        dp[i+1][1] = min(dp[i][1] + X, dp[i][0] + X + Z)

print(min(dp[-1]))
