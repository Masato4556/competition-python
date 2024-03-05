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


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


N, M, K = MAP(int)

n_list = [N * i for i in range(1, 3*K)]
m_list = [M * i for i in range(1, 3*K)]
nm_gcd = gcd(N, M)
nm_list = [nm_gcd * i for i in range(1, 3*K)]

n_ind = 0
m_ind = 0

cnt = 0
while True:
    if n_list[n_ind] < m_list[m_ind]:
        cnt += 1
        cur = n_list[n_ind]
        n_ind += 1
    elif n_list[n_ind] > m_list[m_ind]:
        cnt += 1
        cur = m_list[m_ind]
        m_ind += 1
    else:
        n_ind += 1
        m_ind += 1

    if cnt == K:
        print(cur)
        exit()
