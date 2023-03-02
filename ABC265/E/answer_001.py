# 998244353
from collections import defaultdict


n, m = map(int, input().split())
a, b, c, d, e, f = map(int, input().split())
moves = [(a, b), (c, d), (e, f)]

objects = {tuple(map(int, input().split())) for _ in range(m)}

dp = [defaultdict(int) for _ in range(n+1)]

dp[0][(0,0)] = 1

for i in range(n):
    for curr_pos in dp[i]:
        for move in moves:
            next_pos = (curr_pos[0] + move[0], curr_pos[1] + move[1])
            if next_pos in objects: continue

            dp[i+1][next_pos] += dp[i][curr_pos]
            dp[i+1][next_pos] %= 998244353

ans = 0
for cnt in dp[-1].values():
    ans += cnt
    ans %= 998244353
print(ans)