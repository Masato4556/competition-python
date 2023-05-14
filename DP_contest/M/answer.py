MOD = 10**9 + 7 

def cumulative_sum(array):
    n = len(array)
    cumsum = [0] * (n+1)
    for i in range(n):
        cumsum[i+1] = cumsum[i] + array[i]
    return cumsum

N, K = map(int, input().split())
A = list(map(int, input().split()))

if K == 0:
    print(1)
    exit()

dp = [[0] * (K+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    s = cumulative_sum(dp[i-1])
    for j in range(K+1):
        dp[i][j] = (s[j+1] - s[max(0, j-A[i-1])]) % MOD

print(dp[N][K])
