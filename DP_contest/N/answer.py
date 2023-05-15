
N = int(input())
A = list(map(int, input().split()))

INF = 10**18

def cumulative_sum(array):
    n = len(array)
    cumsum = [0] * (n+1)
    for i in range(n):
        cumsum[i+1] = cumsum[i] + array[i]
    return cumsum

s = cumulative_sum(A)
dp = [[INF for _ in range(N)] for _ in range(N)]


for i in range(N):
    dp[i][i] = 0

for i in range(1, N):
    for j in range(N-i):
        base = s[j+i+1] - s[j]
        for k in range(i):
            dp[j][j+i] = min(dp[j][j+i], base + dp[j][j+k] + dp[j+k+1][j+i])
        
print(dp[0][-1])
