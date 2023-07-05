N, K, D = map(int, input().split())
A = list(map(int, input().split()))

dp = [[[-1] * D for _ in range(K+1)] for _ in range(N+1)]
dp[0][0][0] = 0


for i in range(N):
    a = A[i]
    for k in range(K+1):
        for d in range(D):
            if dp[i][k][d] == -1:
                continue
            dp[i+1][k][d] = max(dp[i+1][k][d], dp[i][k][d])

            if k < K:
                dp[i+1][k+1][(d+a)%D] = max(dp[i+1][k+1][(d+a)%D], dp[i][k][d] + a)

print(dp[N][K][0])