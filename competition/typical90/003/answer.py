from collections import deque
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


N = INT()
G = defaultdict(list)
for _ in range(N-1):
    a, b = MAP(lambda x: int(x)-1)
    G[a].append(b)
    G[b].append(a)


# 到達可能かを調べる
def bfs(graph, start):
    # 訪問済みのノードを管理するための集合
    visited = set()
    # 訪問予定のノードを管理するためのキュー
    queue = deque([start])

    while queue:
        # キューの先頭からノードを取り出す
        node = queue.popleft()
        # 取り出したノードが訪問済みでなければ、訪問済みにする
        if node not in visited:
            visited.add(node)
            # 取り出したノードに隣接するノードをキューに追加する
            queue.extend(graph[node] - visited)

    # 訪問済みのノードを返す
    return visited


def bfs_dist(graph, start):
    # 各ノードについて、そこまでの最短経路の長さを保持するための辞書
    dist = [-1] * len(graph)
    # キューに開始ノードを追加する
    queue = deque([start])
    dist[start] = 0

    while queue:
        v = queue.popleft()
        for next_v in graph[v]:
            if dist[next_v] != -1:
                continue
            dist[next_v] = dist[v] + 1
            queue.append(next_v)

    return dist, v


_, v = bfs_dist(G, 0)
longest_dist, u = bfs_dist(G, v)
print(longest_dist[u]+1)
