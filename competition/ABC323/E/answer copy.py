
MOD = 998244353
N, X = map(int, input().split())
T = list(map(int, input().split()))

dp = [0 for _ in range(X+1)]
dp[0] = 1

ans = 0
divn = pow(N, MOD - 2, MOD)
for i in range(X+1):
    if dp[i] == 0:
        continue
    for j in range(N):
        if i+T[j] > X:
            if j == 0:
                ans += dp[i] * divn
                ans %= MOD
            continue
        dp[i+T[j]] += dp[i] * divn
        dp[i+T[j]] %= MOD

print(ans)
