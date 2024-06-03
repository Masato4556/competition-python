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
jobs = [TUPLE(int) for _ in range(N)]
jobs.sort()

dp = [{0: 0}]
for job in jobs:
    dp.append(dict())

    d, c, s = job
    for prev_c, prev_s in dp[-2].items():
        # この仕事をしなかった場合
        if prev_c not in dp[-1] or prev_s > dp[-1][prev_c]:
            dp[-1][prev_c] = prev_s

        # この仕事をした場合
        if prev_c + c > d:
            continue
        if (prev_c + c) not in dp[-1] or prev_s + s > dp[-1][prev_c + c]:
            dp[-1][prev_c + c] = prev_s + s

print(max(dp[-1].values()))
