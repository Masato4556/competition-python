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


MOD = 10**9 + 7

N = INT()
S = input()

valid_chars = {"a", "t", "c", "o", "d", "e", "r"}
conv = {"a": 0, "t": 1, "c": 2, "o": 3, "d": 4, "e": 5, "r": 6}
S = [conv[c] for c in S if c in valid_chars]
N = len(S)

dp = [[0] * 7 for _ in range(N+1)]

for i in range(N):
    for j in range(7):
        dp[i+1][j] = dp[i][j]
    if S[i] == 0:
        dp[i+1][0] += 1
        dp[i+1][0] %= MOD
    else:
        dp[i+1][S[i]] += dp[i][S[i]-1]
        dp[i+1][S[i]] %= MOD

print(dp[N][6])
