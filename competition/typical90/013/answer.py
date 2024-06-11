import sys
from atcoder import lazysegtree
from atcoder.string import suffix_array
from bisect import bisect, bisect_left, insort, insort_left
from collections import deque, defaultdict, Counter
from copy import deepcopy
from functools import lru_cache
import heapq
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


def dijkstra(adj_list, start):
    """
    adj_list: 隣接リストを表す辞書型データ構造 {u: [(v, cost), ... ], ... }
    start: 始点の頂点番号
    """
    n = len(adj_list)
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]
    heapq.heapify(heap)

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, cost in adj_list[u]:
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                heapq.heappush(heap, (dist[v], v))

    return dist


N, M = MAP(int)

G = [set() for _ in range(N)]
for _ in range(M):
    a, b, c = MAP(int)
    a -= 1
    b -= 1
    G[a].add((b, c))
    G[b].add((a, c))


cost1 = dijkstra(G, 0)
cost2 = dijkstra(G, N-1)

for k in range(N):
    print(cost1[k] + cost2[k])
