N, M, K = map(int, input().split())
mod = 998244353
p = pow(M, mod-2, mod)

dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
dp[0][0] = 1

for k in range(1, K+1):
    for n in range(N+1):
        for m in range(1, M+1):
            if n+m > N:
                dp[k][N - (n + m - N)] += dp[k-1][n] * p
                dp[k][N - (n + m - N)] %= mod
            else:
                dp[k][n+m] += dp[k-1][n] * p
                dp[k][n+m] %= mod

ans = 0
for k in range(K+1):
    ans += dp[k][-1] * p
    ans %= mod
print(ans)

for d in dp:
    print(d)
