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
def GRID(n): return [input() for _ in range(n)]
def ZIP(n, func=f): return zip(*(MAP(func) for _ in range(n)))


L, R = MAP(int)


def f(l, r):
    if r - l < 0:
        print("error", l, r)
        exit()
    i = floor(log2(r-l))
    j = floor(l / (2**i))

    print(l, r, i, j)

    while i >= 0:
        while not (l <= (2 ** i) * j < r):
            print(i, j)
            j += 1

        if l <= (2 ** i) * (j+1) <= r:
            temp = []
            print("i:j", i, j)
            # print("======", l, r)
            if l != (2 ** i) * j:
                # print("a", l, (2 ** i) * j)
                temp.extend(f(l, (2 ** i) * j))
            temp.append(((2 ** i) * j, (2 ** i) * (j+1)))
            if (2 ** i) * (j+1) != r:
                # print("b", (2 ** i) * (j+1), r)
                temp.extend(f((2 ** i) * (j+1), r))
            return temp

        i -= 1

    return "error"


ans = f(L, R)
print(len(ans))
for a in ans:
    print(*a)
