from collections import defaultdict
from functools import lru_cache
import sys

sys.setrecursionlimit(10**6)

@lru_cache(None)
def f(a, b, c, n):
    global aa
    s = a+b+c
    if s == 0:
        return 0
    ret = n
    if a != 0:
        ret += f(a-1, b, c, n) * a
    if b != 0:
        ret += f(a+1, b-1, c, n) * b
    if c != 0:
        ret += f(a, b+1, c-1, n) * c
    return ret / s


N = int(input())
cnts = defaultdict(int)
for a in map(int, input().split()):
    cnts[a] += 1

print(f(cnts[1], cnts[2], cnts[3], N))
