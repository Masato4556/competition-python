from collections import defaultdict

MOD = 10**9 + 7 

N, K = map(int, input().split())
A = list(map(int, input().split()))


dp = [defaultdict(int) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    # print(f"子供{i}人")
    for prev_k, prev_v in dp[i-1].items():
        # print(prev_k, K-prev_k+1, A[i-1]+1)
        for j in range(min(K-prev_k+1, A[i-1]+1)):
            # print(i, j, prev_k)
            dp[i][prev_k+j] += prev_v
            dp[i][prev_k+j] %= MOD
        
print(dp[N][K])
# print(dp)