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
A = list(set(LIST(int)))
M = INT()
B = list(set(LIST(int)))
L = INT()
C = list(set(LIST(int)))
Q = INT()
X = LIST(int)

ab_sums = set()
for a in A:
    for b in B:
        ab_sums.add(a+b)

abc_sums = set()
for ab in ab_sums:
    for c in C:
        abc_sums.add(ab+c)

for x in X:
    print("Yes" if x in abc_sums else "No")
