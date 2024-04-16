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


def rot90(a):
    return list(zip(*reversed(a)))


pats = [
    [
        [1, 0, 1],
        [1, 1, 0],
        [0, 1, 0]
    ],
    [
        [1, 0, 1],
        [1, 0, 0],
        [0, 1, 1]
    ],
    [
        [1, 0, 1],
        [1, 0, 1],
        [0, 1, 0]
    ],
    [
        [1, 0, 1],
        [0, 1, 1],
        [0, 1, 0]
    ],
]


def calc(a, pat):
    Takahashi, Aoki = 0, 0
    for i in range(3):
        for j in range(3):
            if pat[i][j]:
                Takahashi += a[i][j]
            else:
                Aoki += a[i][j]
    return Takahashi, Aoki


A = GRID(3)
ta_count = 0
for _ in range(4):
    for pat in pats:
        ta, ao = calc(A, pat)
        ta_count += 1 if ta > ao else 0
    A = rot90(A)

# print(ta_count)
print("Takahashi" if ta_count >= 4 else "Aoki")
