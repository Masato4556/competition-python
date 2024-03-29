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


def print_grid(grid):
    for g in grid:
        print(g)


def validate(i, piece_ids):
    grid = [[0] * W for _ in range(H)]
    pos_ind = 0
    for piece_id in piece_ids:

        pos_x = pos_ind % W
        pos_y = pos_ind // W
        piece_h, piece_w = pieces[piece_id]
        if i >> piece_id & 1:
            piece_h, piece_w = piece_w, piece_h

        for x in range(pos_x, pos_x+piece_w):
            for y in range(pos_y, pos_y+piece_h):
                if x >= W or y >= H:
                    return False
                if grid[y][x] == 1:
                    return False
                grid[y][x] = 1

        while pos_ind < H * W and grid[pos_ind // W][pos_ind % W] == 1:
            pos_ind += 1

        if pos_ind == H * W:
            break

    return all(grid[i][j] == 1 for i in range(H) for j in range(W))


for i in range(2**N):
    for p in permutations(range(N), N):
        if validate(i, p):
            print("Yes")
            exit()

print("No")

# print(validate(0, range(N)))
# (0,0),(0,1),(0.2) ... (H-1, W-1)と順に見て、一番初めに出てくる空いているマスを見つける
# そのマスを埋めるようにピースを置く
# これを繰り返す

# ピースの順番とピースの奥向きのパターン数は N! * 2**N。全探索が可能そう
