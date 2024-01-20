
from collections import defaultdict, deque
import heapq

from functools import lru_cache


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])  # 経路圧縮
            return self.par[x]

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return False
        # union by rank
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.par[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry]
        return True

    def size(self, x):
        return self.siz[self.root(x)]

    def roots(self):
        return [i for i, x in enumerate(self.par) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):  # Debug用メソッド　計算量多いので使わないように
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.root(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


def bfs_dist(graph, n, start):
    dist = [0] * n
    queue = deque([start])
    dist[start] = 1

    while queue:
        v = queue.popleft()
        for next_v in graph[v]:
            if dist[next_v] >= dist[v] + 1:
                continue
            dist[next_v] = dist[v] + 1
            queue.append(next_v)

    return dist


N, M = map(int, input().strip().split())
A = list(map(int, input().strip().split()))

G = defaultdict(set)
uf = UnionFind(N)

edges = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]

for u, v in edges:
    if A[u] == A[v]:
        uf.unite(u, v)


@lru_cache(None)
def root(v):
    return uf.root(v)


for u, v in edges:
    u = root(u)
    v = root(v)
    if u == v:
        continue

    if A[u] < A[v]:
        G[u].add(v)
    elif A[u] > A[v]:
        G[v].add(u)


# print(20945)
dist = bfs_dist(G, N, uf.root(0))
print(dist[uf.root(N-1)])
