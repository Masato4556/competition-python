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
def MAP(func=f): return map(func, input().split())
def LIST(func=f): return list(map(func,  input().split()))
def TUPLE(func=f): return tuple(map(func, input().split()))
def GRID(n): return [input() for _ in range(n)]
def ZIP(n, func=f): return zip(*(MAP(func) for _ in range(n)))


N, H, W = MAP(int)
pieces = [TUPLE(int) for _ in range(N)]


que = deque([(0, set())])

while que:
    piece_ind, s = que.popleft()

    if piece_ind == N:
        if len(s) == H * W:
            print("Yes")
            exit()
        continue

    piece = pieces[piece_ind]

    que.append((piece_ind+1, s))

    for x in range(W - piece[0] + 1):
        for y in range(W - piece[1] + 1):
            new_s = s.copy()
            for i in range(x, x+piece[0]):
                for j in range(y, y+piece[1]):
                    new_s.add((i, j))
            if len(new_s) == len(s) + piece[0] * piece[1]:
                que.append((piece_ind+1, new_s))

    for x in range(W - piece[1] + 1):
        for y in range(W - piece[0] + 1):
            new_s = s.copy()
            for i in range(x, x+piece[0]):
                for j in range(y, y+piece[1]):
                    new_s.add((i, j))
            if len(new_s) == len(s) + piece[0] * piece[1]:
                que.append((piece_ind+1, new_s))

print("No")
