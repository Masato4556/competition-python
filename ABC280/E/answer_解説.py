MOD = 998244353
denominator = pow(100, MOD - 2, MOD)

N, P = map(int, input().split())

dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    dp[i] = ((dp[i-1]+1) * (100-P) + (dp[max(0, i-2)]+1) * P) * denominator % MOD

print(dp[N])
