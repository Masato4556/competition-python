import sys
from atcoder import lazysegtree
from atcoder.string import suffix_array
from bisect import bisect, bisect_left, insort, insort_left
from collections import deque, defaultdict, Counter
from copy import deepcopy
from functools import lru_cache
from heapq import heappush, heappop, heapify
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from math import ceil, floor, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, atan2, radians, degrees, log2, gcd, perm, comb
INF = float('inf')
sys.setrecursionlimit(10**9)
def f(x): return x
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(func=f): return map(func, input().split())
def LIST(func=f): return list(map(func, input().split()))
def TUPLE(func=f): return tuple(map(func, input().split()))
def GRID(n): return [input() for _ in range(n)]
def ZIP(n, func=f): return zip(*(MAP(func) for _ in range(n)))


N = INT()
jobs = dict()
for _ in range(N):
    d, c, s = MAP(int)
    if d not in jobs:
        jobs[d] = []
    jobs[d].append((c, s))

ds = [0]
for d in jobs.keys():
    ds.append(d)
ds.sort()
print(len(ds), len(set(ds)))

dp = [{0: 0}]

for d_i in range(1, len(ds)):
    d = ds[d_i]

    dp.append(dict())
    for prev_c, prev_s in dp[d_i-1].items():
        if prev_c not in dp[d_i] or prev_s > dp[d_i][prev_c]:
            dp[d_i][prev_c] = prev_s

        for c, s in jobs[d]:
            if prev_c + c > d:
                continue
            if (prev_c + c) not in dp[d_i] or prev_s + s > dp[d_i][prev_c + c]:
                dp[d_i][prev_c + c] = prev_s + s

print(max(dp[-1].values()))
