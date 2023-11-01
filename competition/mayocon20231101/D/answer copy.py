N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

INF = 10**18

dp = [[INF for _ in range(M+1)] for _ in range(N+1)]
dp[0][0] = 0

ans = 0
max_t = 0
for i in range(N+1):
    for j in range(M+1):
        if i > 0:
            dp[i][j] = min(dp[i][j], dp[i-1][j] + A[i-1])
        if j > 0:
            dp[i][j] = min(dp[i][j], dp[i][j-1] + B[j-1])

        if dp[i][j] > K:
            break

        ans = i+j


print(ans)