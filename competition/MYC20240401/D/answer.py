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
# def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(func=f): return map(func, input().split())
def LIST(func=f): return list(map(func,  input().split()))
def TUPLE(func=f): return tuple(map(func, input().split()))
def GRID(n): return [input() for _ in range(n)]
def ZIP(n, func=f): return zip(*(MAP(func) for _ in range(n)))


N = INT()
M = ceil(log2(N))
print(M)

reqs = [list() for _ in range(M)]
for i in range(N):
    for j in range(M):
        if i >> j & 1:
            reqs[j].append(i+1)

for req in reqs:
    print(len(req), *req)

S = list(map(int, input()))

ans = 0
for i in range(M):
    if S[i] == 0:
        continue
    ans += 2**i

print(ans+1)
