
N = int(input())

G = []
for i in range(N-1):
    a, b, x = map(int, input().split())
    x -= 1
    G.append((a, b, x))

dp = [float('inf')] * (N)
dp[0] = 0

for i in range(N-1):
    a, b, x = G[i]
    dp[i+1] = min(dp[i+1], dp[i] + a)
    dp[x] = min(dp[x], dp[i] + b)

print(dp)
print(dp[-1])
