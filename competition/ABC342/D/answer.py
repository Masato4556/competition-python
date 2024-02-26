import sys
from atcoder import lazysegtree
from atcoder.string import suffix_array
from bisect import bisect, bisect_left, insort, insort_left
from collections import deque, defaultdict, Counter
from copy import deepcopy
from functools import lru_cache
from heapq import heappush, heappop, heapify
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from math import ceil, floor, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, atan2, radians, degrees, log2, gcd, prod
from functools import lru_cache

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


@lru_cache(None)
def prime_factorize(n):
    ret = []
    i = 2
    while i**2 <= n:
        e = 0
        while n % i == 0:
            n //= i
            e += 1
        if e > 0:
            ret.append((i, e))
        i += 1
    if n > 1:
        ret.append((n, 1))
    return ret


N = INT()
A = LIST(int)


required_number = []
for a in A:
    if a == 0:
        required_number.append(0)
    else:
        required_number.append(
            prod([p[0] for p in prime_factorize(a) if p[1] % 2 == 1]))

counter = Counter(required_number)
ans = 0
for v, cnt in counter.items():
    if v == 0:
        continue
    ans += cnt * (cnt-1) // 2


c = 0
for i in range(N):
    if A[i] != 0:
        continue
    ans += N-1 - c
    c += 1


print(ans)


# # テスト用
# ans = 0
# for i in range(N-1):
#     for j in range(i+1, N):
#         if required_number[i] == 0 or required_number[j] == 0:
#             ans += 1
#         elif required_number[i] == required_number[j]:
#             ans += 1
# print(ans)
