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

que = [(0, 0)]
ans = 9999
while len(que):
    cur, num = heappop(que)

    mod = (N - cur) % coins[2]
    div = (N - cur) // coins[2]

    if mod == 0 and num + div < ans:
        ans = num + div

    if num >= ans:
        continue

    for i in range(2):
        nex = cur + coins[i]
        if nex > N:
            continue
        heappush(que, (nex, num+1))
        print(que)

print(ans)
