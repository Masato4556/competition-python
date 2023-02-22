N, M, K = map(int, input().split())
mod = 998244353

dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
dp[0][0] = 1

for k in range(1, K+1):
    for n in range(N):
        for m in range(1, M+1):
            if n+m > N:
                dp[k][N - (n + m - N)] += dp[k-1][n] % mod
            else:
                dp[k][n+m] += dp[k-1][n] % mod

ans = 0
for k in range(K+1):
    a = m ** k % mod
    ans += (dp[k][-1] * pow(a, mod - 2, mod)) % mod
print(ans % mod)
