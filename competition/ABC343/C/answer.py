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

cubic_nums = []

x = 0
while True:
    x += 1
    cubic_x = x**3
    if x**3 > N:
        break
    cubic_nums.append(cubic_x)

cubic_nums.reverse()

for v in cubic_nums:
    s = str(v)
    is_valid = True
    for i in range(len(s) // 2):
        if s[i] != s[len(s)-i-1]:
            is_valid = False
            break

    if is_valid:
        print(s)
        exit()
