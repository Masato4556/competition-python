from collections import defaultdict

N = int(input())
P = list(map(float, input().split()))

dp = [defaultdict(float) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    for k, v in dp[i-1].items():
        dp[i][k+1] += v * P[i-1]
        dp[i][k-1] += v * (1 - P[i-1])

ans = 0
for k, v in dp[-1].items():
    if k <= 0:
        continue
    ans += v
print(ans)
