N = int(input())

dp = [[-1] * 3 for _ in range(N)]
dp[0] = list(map(int, input().split()))

for i in range(1, N):
    h = list(map(int, input().split()))
    for j in range(3):
        for k in range(3):
            if j == k: continue
            dp[i][k] = max(dp[i][k], dp[i-1][j] + h[k])

print(max(dp[-1]))
