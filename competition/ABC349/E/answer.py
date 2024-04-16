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
def LIST(func=f): return list(map(func,  input().split()))
def TUPLE(func=f): return tuple(map(func, input().split()))
def GRID(n): return [LIST(int) for _ in range(n)]
def ZIP(n, func=f): return zip(*(MAP(func) for _ in range(n)))


A = GRID(3)


@lru_cache(None)
def check(g):
    for i in range(3):
        if g[i*3 + 0] != 0 and g[i*3 + 0] == g[i*3 + 1] == g[i*3 + 2]:
            return g[i*3 + 0]
        if g[0*3 + i] != 0 and g[0*3 + i] == g[1*3 + i] == g[2*3 + i]:
            return g[0*3 + i]
    if g[0*3 + 0] != 0 and g[0*3 + 0] == g[1*3 + 1] == g[2*3 + 2]:
        return g[0*3 + 0]
    if g[0*3 + 2] != 0 and g[0*3 + 2] == g[1*3 + 1] == g[2*3 + 0]:
        return g[0*3 + 2]

    if (g.count(0)) == 0:
        score = defaultdict(int)
        for x in range(3):
            for y in range(3):
                score[g[y*3 + x]] += A[y][x]
        return 1 if score[1] > score[2] else 2

    return 0


@lru_cache(None)
def f(g, i):

    result = check(g)
    if result != 0:
        return result

    fill_num = 1 if i % 2 == 0 else 2
    results = []
    for x in range(3):
        for y in range(3):
            if g[y*3 + x] == 0:
                cur_g = list(deepcopy(g))
                cur_g[y*3 + x] = fill_num
                results.append(f(tuple(cur_g), i+1))
    return fill_num if results.count(fill_num) else 3-fill_num


print("Takahashi" if f((0, 0, 0, 0, 0, 0, 0, 0, 0,), 0) == 1 else "Aoki")
