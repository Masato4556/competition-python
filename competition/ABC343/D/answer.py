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
def MAP(func): return map(func, input().split())
def LIST(func=f): return list(map(func,  input().split()))
def TUPLE(func=f): return tuple(map(func, input().split()))
def GRID(n): return [input() for _ in range(n)]
def ZIP(n, func=f): return zip(*(MAP(func) for _ in range(n)))


N, T = MAP(int)

points = [0] * N
score_cnt = defaultdict(int)
score_cnt[0] = N

uniq_score = set([0])

for i in range(T):
    a, b = MAP(int)
    a -= 1

    score_cnt[points[a]] -= 1
    if score_cnt[points[a]] == 0:
        uniq_score.remove(points[a])
    points[a] += b
    score_cnt[points[a]] += 1
    uniq_score.add(points[a])
    print(len(uniq_score))
