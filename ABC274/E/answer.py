from math import dist
INF = 10**18

n, m = map(int, input().split())

dp = [[[INF] for _ in range(2**(n+m+1))] for _ in range(n+m+1)]

pos = []
for i in range(n+m):
    x, y = map(int, input().split())
    pos.append((x, y))

    dp[i][0] = dist((0, 0), (x, y))

for i in range(n+m):
    dp[]
print(dp)
