import sys
from atcoder import lazysegtree
from atcoder.string import suffix_array
from bisect import bisect, bisect_left, insort, insort_left
from collections import deque, defaultdict, Counter
from copy import deepcopy
from functools import lru_cache
from heapq import heappush, heappop, heapify
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from math import ceil, floor, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, atan2, radians, degrees, log2, gcd
INF = float('inf')
sys.setrecursionlimit(10**9)
def f(x): return x
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(func=f): return map(func, input().split())
def LIST(func=f): return list(map(func,  input().split()))
def TUPLE(func=f): return tuple(map(func, input().split()))
def GRID(n): return [input() for _ in range(n)]
def ZIP(n, func=f): return zip(*(MAP(func) for _ in range(n)))


T = input()
N = INT()
dp = defaultdict(lambda: INF)
dp[""] = 0

valid_pattern = set()
for i in range(len(T)+1):
    valid_pattern.add(T[0:i])

for _ in range(N):
    a, *S = MAP()

    temp = defaultdict(lambda: INF)

    for prev in dp:
        for s in S:
            if prev+s not in valid_pattern:
                continue
            temp[prev+s] = min(temp[prev+s], dp[prev]+1)

    for k, v in temp.items():
        dp[k] = min(dp[k], v)

print(-1 if dp[T] == INF else dp[T])
