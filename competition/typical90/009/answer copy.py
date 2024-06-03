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


N = INT()
poses = [LIST(float) for _ in range(N)]

ans = Decimal('0')
for i, j, k in combinations(range(N), 3):
    x1, y1 = poses[i]
    x2, y2 = poses[j]
    x3, y3 = poses[k]

    vec1 = [x1 - x2, y1 - y2]
    vec2 = [x3 - x2, y3 - y2]

    dot_product = vec1[0] * vec2[0] + vec1[1] * vec2[1]
    magnitude1 = (vec1[0] ** 2 + vec1[1] ** 2) ** 0.5
    magnitude2 = (vec2[0] ** 2 + vec2[1] ** 2) ** 0.5

    cos_theta = dot_product / magnitude1 / magnitude2

    d = degrees(acos(cos_theta))

    if d > ans:
        ans = d

print(ans)

# これは組み合わせを使って全探索するだけ
# なぜか大きい誤差が生じる。実装ミスかも
