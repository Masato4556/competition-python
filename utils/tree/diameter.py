import sys
from collections import deque
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


def tree_diameter(G):
    def bfs(start):
        dists = [-1] * len(G)
        dists[start] = 0
        que = deque([start])
        while que:
            v = que.popleft()
            for u, cost in G[v]:
                if dists[u] == -1:
                    dists[u] = dists[v] + cost
                    que.append(u)
        max_v = dists.index(max(dists))
        return max_v, dists
    u, _ = bfs(0)
    v, dists = bfs(u)
    diameter = dists[v]
    path = [v]
    while v != u:
        for next_v, cost in G[v]:
            if dists[next_v] + cost == dists[v]:
                path.append(next_v)
                v = next_v
                break
    return diameter, path


def solve():
    N = INT()
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b, c = MAP(int)
        G[a].append((b, c))
        G[b].append((a, c))
    diameter, path = tree_diameter(G)
    print(diameter, len(path))
    print(*path)


# PROBLEM: https://judge.yosupo.jp/problem/tree_diameter
solve()
