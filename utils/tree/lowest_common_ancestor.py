import sys
from collections import deque
sys.setrecursionlimit(10**9)
def f(x): return x
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(func=f): return map(func, input().split())
def LIST(func=f): return list(map(func, input().split()))
def TUPLE(func=f): return tuple(map(func, input().split()))
def GRID(n): return [input() for _ in range(n)]
def ZIP(n, func=f): return zip(*(MAP(func) for _ in range(n)))


def init_lca(G, root):
    N = len(G)
    log_N = (N-1).bit_length()
    parents = [[-1] * N for _ in range(log_N)]
    depths = [-1] * N
    depths[root] = 0
    que = deque([root])
    while que:
        v = que.popleft()
        for u in G[v]:
            if depths[u] == -1:
                depths[u] = depths[v] + 1
                parents[0][u] = v
                que.append(u)
    for k in range(log_N-1):
        for v in range(N):
            if parents[k][v] == -1:
                parents[k+1][v] = -1
            else:
                parents[k+1][v] = parents[k][parents[k][v]]
    return parents, depths


def query_lca(v, u, parents, depths):
    if depths[v] < depths[u]:
        v, u = u, v
    log_N = len(parents)
    for k in range(log_N):
        if (depths[v] - depths[u]) >> k & 1:
            v = parents[k][v]
    if v == u:
        return v
    for k in range(log_N-1, -1, -1):
        if parents[k][v] != parents[k][u]:
            v = parents[k][v]
            u = parents[k][u]
    return parents[0][v]


def solve():

    N, Q = MAP(int)
    P = LIST(int)
    G = [[] for _ in range(N)]
    for i, p in enumerate(P):
        G[i+1].append(p)
        G[p].append(i+1)

    parents, depths = init_lca(G, 0)

    for _ in range(Q):
        u, v = MAP(int)
        print(query_lca(u, v, parents, depths))


# https://judge.yosupo.jp/problem/lca
solve()


# copilotに書いてもらったコードなので、しっかりと熟読して理解すること
