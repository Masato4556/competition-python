from collections import defaultdict
from functools import lru_cache

n, m = map(int, input().split())
a, b, c, d, e, f = map(int, input().split())
moves = [(a, b), (c, d), (e, f)]

objects = {tuple(map(int, input().split())) for _ in range(m)}

dp = defaultdict(int)
dp[(0,0)] = 1

@lru_cache(None)
def f(x, y):
    return [(x + move[0], y + move[1]) for move in moves if (x + move[0], y + move[1]) not in objects]

for i in range(n):
    new_dp = defaultdict(int)
    for curr_pos in dp.keys():
        for next_pos in f(curr_pos[0], curr_pos[1]):
            new_dp[next_pos] += dp[curr_pos]
            new_dp[next_pos] %= 998244353
    dp = new_dp

ans = 0
for cnt in dp.values():
    ans += cnt
    ans %= 998244353
print(ans)