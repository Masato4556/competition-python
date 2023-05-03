from functools import lru_cache
import sys
sys.setrecursionlimit(10 ** 9)

N, M = map(int, input().split())
G = [set() for _ in range(N)]
for _ in range(M):
    x, y = map(lambda x: int(x)-1, input().split())
    G[x].add(y)

@lru_cache(None)
def f(v):
    global G
    dist = 0
    for next_v in G[v]:
        dist = max(dist, f(next_v) + 1)
    return dist

ans = 0
for i in range(N):
    ans = max(ans, f(i))
print(ans)