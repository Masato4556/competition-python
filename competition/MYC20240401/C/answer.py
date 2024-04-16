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


def topological_sort(G, in_degs):
    que = deque()
    is_sorted_uniquely = True
    n = len(G)

    # 入次数が0のノードをキューに追加
    for i in range(n):
        if in_degs[i] == 0:
            que.append(i)

    order = []
    while que:
        if len(que) > 1:
            is_sorted_uniquely = False
        v = que.popleft()
        order.append(v)
        for adj in G[v]:
            in_degs[adj] -= 1
            if in_degs[adj] == 0:  # 入次数が0になったら、キューに入れる
                que.append(adj)

    has_cycles = len(order) != n  # サイクルが存在する場合、
    return (order, is_sorted_uniquely, has_cycles)


N = INT()

converter = dict()
ind = -1
edges = []
for i in range(N):
    S, T = MAP()
    if S not in converter:
        ind += 1
        converter[S] = ind
    if T not in converter:
        ind += 1
        converter[T] = ind
    edges.append((converter[S], converter[T]))

G = [list() for _ in range(len(converter.keys()))]
indegs = [0 for _ in range(len(converter.keys()))]

for edge in edges:
    S, T = edge
    G[S].append(T)
    indegs[T] += 1

_, _, has_cycles = topological_sort(G, indegs)
print("Yes" if not has_cycles else "No")
