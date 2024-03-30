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


def popcount(x):
    x = x - ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 0x0000007f


a, b, C = MAP(int)

c_bit_num = len(bin(C))-2
c = popcount(C)
X = 0
Y = 0

# if (a + b - c) % 2 != 0:
#     print(-1)
#     exit()

cnt = (a + b - c) // 2

# print(a, b, c)
# print(cnt)

for i in range(c_bit_num):
    if C >> i & 1:
        if a < b:
            b -= 1
            Y += 2**i
        else:
            a -= 1
            X += 2**i
    else:
        if a > 0 and b > 0 and cnt > 0:
            a -= 1
            b -= 1
            X += 2**i
            Y += 2**i
            cnt -= 1


if a != b:
    print(-1)
    exit()
if a + c_bit_num > 60:
    print(-1)
    exit()

for i in range(c_bit_num, c_bit_num + a):
    X += 2**i
    Y += 2**i

print(X, Y)
