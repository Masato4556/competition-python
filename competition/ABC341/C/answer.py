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


H, W, N = MAP(int)
T = input()
S = GRID(H)


def move(pos, t):
    if t == "U":
        return (pos[0], pos[1]-1)
    elif t == "D":
        return (pos[0], pos[1]+1)
    elif t == "R":
        return (pos[0]+1, pos[1])
    elif t == "L":
        return (pos[0]-1, pos[1])


def check(x, y):
    pos = (x, y)
    if S[pos[1]][pos[0]] == "#":
        return False
    for t in T:
        pos = move(pos, t)
        if not (0 <= pos[0] < W and 0 <= pos[1] < H):
            return False
        if S[pos[1]][pos[0]] == "#":
            return False
    return True


ans = 0
for y in range(H):
    for x in range(W):
        if check(x, y):
            ans += 1

print(ans)
