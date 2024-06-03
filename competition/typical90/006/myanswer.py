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


N, K = MAP(int)
S = input()

cumsums = [[] for _ in range(K)]
cumsums[0].append(S[-1])
for i in range(N-1):
    s = S[N-2-i]
    if s < cumsums[0][i]:
        cumsums[0].append(s)
    else:
        cumsums[0].append(cumsums[0][-1])

cumsums[0].reverse()

for i in range(1, K):
    cumsums[i] = []
    for j in range(N-i-1, -1, -1):
        if j == N-i-1:
            cumsums[i].append(S[j]+cumsums[i-1][j+1])
            continue
        a = S[j]+cumsums[i-1][j+1]
        b = cumsums[i][-1]
        if a < b:
            cumsums[i].append(a)
        else:
            cumsums[i].append(b)

    cumsums[i].reverse()


print(cumsums[-1][0])
