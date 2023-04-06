import sys
from functools import lru_cache

sys.setrecursionlimit(10**6)

N = int(input())

@lru_cache(None)
def dfs(n, v):
    if n >= N: 
        return v

    vv = 0
    for i in range(1, 6 + 1):
        vv += dfs(n+1, i)
    vv /= 6

    return vv if vv > v else v

ans = dfs(0, 0)
print(ans)

