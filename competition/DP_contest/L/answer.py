import sys
sys.setrecursionlimit(10**9)

N = int(input())
A = list(map(int, input().split()))
cnt = 0

dp = [[-1] *  (N) for _ in range(N)]

for i in range(N):
    dp[i][i] = A[i]

for i in range(1, N):
    for l in range(N - i):
        r = l + i
        dp[l][r] = max(dp[l][l] - dp[l+1][r], dp[r][r] - dp[l][r-1])

print(dp[0][N-1])
