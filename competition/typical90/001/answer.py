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


def solve():
    def binary_search(f, lo, hi):
        left = lo  # f(x) == trueとなる最大のx
        right = hi  # f(x) == falseとなる最小のx
        assert f(lo), "探索範囲に境界値が含まれていません"
        assert not f(hi), "探索範囲に境界値が含まれていません"

        while right - left > 1:
            mid = (left + right) // 2
            if f(mid):
                left = mid
            else:
                right = mid
        return left

    N, L = MAP(int)
    K = INT()
    A = LIST(int)

    A_dist = []
    prev = 0
    for a in A:
        A_dist.append(a - prev)
        prev = a
    A_dist.append(L - prev)

    def f(x):
        dist = 0
        cnt = 0
        for a in A_dist:
            dist += a
            if dist >= x:
                dist = 0
                cnt += 1

        return cnt > K

    print(binary_search(f, min(A_dist), L+1))


solve()
