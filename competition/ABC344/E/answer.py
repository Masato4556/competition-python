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


N = INT()
A = LIST(int)
Q = INT()

G = dict()
for i in range(N):
    if i == 0:
        G[A[i]] = (0, A[i+1])
        G[0] = (-1, A[i])
    elif i == N-1:
        G[A[i]] = (A[i-1], -1)
    else:
        G[A[i]] = (A[i-1], A[i+1])
        G[-1] = (A[i], 0)

for _ in range(Q):
    q, *arg = MAP(int)
    if q == 1:
        x, y = arg[0], arg[1]
        x_prev, x_next = G[x]
        G[x_next] = (y, G[x_next][1])
        G[y] = (x, x_next)
        G[x] = (x_prev, y)

    else:
        x = arg[0]
        x_prev, x_next = G[x]
        G[x_prev] = (G[x_prev][0], x_next)
        G[x_next] = (x_prev, G[x_next][1])


v = 0
ans = []
while True:
    if v == -1:
        break
    if v != 0:
        ans.append(v)

    _, v = G[v]

print(*ans)
