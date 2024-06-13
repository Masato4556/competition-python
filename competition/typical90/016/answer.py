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
coins = LIST(int)
coins.sort(reverse=True)
A, B, C = coins

ans = 9999


for i in range(N//A, -1, -1):
    n_a = N - A * i
    if i > ans:
        break
    for j in range(min(n_a//B, ans), -1, -1):
        n_b = n_a - B * j
        k = n_b // C
        if i+j+k > ans:
            break

        if n_b % C == 0:
            ans = min(ans, i+j+k)
print(ans)
