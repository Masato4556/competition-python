N = int(input())

dp = [[-1] * 5 for _ in range(N+1)]
dp[0][0] = 0

prev_T = 0
for i in range(N):
    T, X, A = map(int, input().split())
    diff_T = T - prev_T
    prev_T = T

    for j in range(5):
        
        if dp[i][j] == -1: continue
        for k in range(max(0, j - diff_T), min(5, j + diff_T+1)):
            v = dp[i][j] if k != X else dp[i][j] + A
            dp[i+1][k] = max(dp[i+1][k], v)
            

print(max(dp[-1]))
