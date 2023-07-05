INF = 10**18

n, m = map(int, input().split())
A = list(map(int, input().split()))

# dp[i][j] Ajまでの要素で、部分列の(i+1)まで合計したものの最大値
dp = [[-1 * INF for _ in range(n)] for _ in range(m)]

for i in range(n):
    dp[0][i] = A[i]
    if dp[0][i-1] > dp[0][i]:
        dp[0][i] = dp[0][i-1]

for i in range(1, m):
    for j in range(i, n):
        dp[i][j] = dp[i-1][j-1] + A[j] * (i + 1)
        if dp[i][j-1] > dp[i][j]:
            dp[i][j] = dp[i][j-1]

print(max(dp[-1]))


