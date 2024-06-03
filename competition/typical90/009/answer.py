from math import ceil, floor, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, atan2, radians, degrees, log2, gcd, perm, comb
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from heapq import heappush, heappop, heapify
from functools import lru_cache
from copy import deepcopy
from collections import deque, defaultdict, Counter
from bisect import bisect, bisect_left, insort, insort_left
from atcoder.string import suffix_array
from atcoder import lazysegtree
import sys
from decimal import Decimal, getcontext
from itertools import combinations
from math import degrees

# 精度を設定
getcontext().prec = 50

INF = Decimal('inf')
sys.setrecursionlimit(10**9)


def f(x): return x
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(func=f): return map(func, input().split())
def LIST(func=f): return list(map(func, input().split()))
def TUPLE(func=f): return tuple(map(func, input().split()))
def GRID(n): return [input() for _ in range(n)]
def ZIP(n, func=f): return zip(*(MAP(func) for _ in range(n)))


def angle(a, b, c, d):
    x = c - a
    y = d - b
    return degrees(atan2(y, x))


N = INT()
poses = [LIST(float) for _ in range(N)]

ans = 0
for j in range(N):
    arr = []
    x1, y1 = poses[j]
    for i in range(N):
        if i == j:
            continue
        x2, y2 = poses[i]
        d = angle(x1, y1, x2, y2)
        arr.append(d)
        arr.append(d+360)
    arr.sort()
    for a in arr[:N-1]:
        idx = bisect_left(arr, a + 180)
        ans = max(ans, arr[idx-1] - a)
        ans = max(ans, a + 360 - arr[idx])

print(ans)
