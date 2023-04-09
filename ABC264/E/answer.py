
from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    def root(self, x):
        if self.par[x] == -1: return x
        else:
          self.par[x] = self.root(self.par[x]) # 経路圧縮
          return self.par[x]

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return False
        # union by rank
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.par[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry]
        return True

    def all_group_members(self):
        group_members = defaultdict(set)
        for member in range(self.n):
            group_members[self.root(member)].add(member)
        return group_members

N, M, E = map(int, input().split())

edges = []
for _ in range(E):
    edges.append(map(lambda x: int(x)-1, input().split()))

Q = int(input())
queries = [int(input()) - 1 for _ in range(Q)]
queries_s = set(queries)

uf = UnionFind(N+M)

for i in range(E):
    if i in queries_s: continue
    u, v = edges[i]
    uf.unite(u, v)

ans = []
on = set()
queries.reverse()

cnt= 0
for j in range(N):
    for k in range(N, N+M):
        if uf.issame(j, k):
            on.add(j)
            break
ans.append(len(on))

for i in range(1, Q-1):
    shouldCheck = True
    x = queries[i]
    u, v = edges[x]
    if uf.issame(u, v): shouldCheck = False
    uf.unite(u, v) 

    if shouldCheck:
        cnt = 0
        for j in range(N):
            for k in range(N, N+M):
                if uf.issame(j, k):
                    on.add(j)
                    break
    ans.append(len(on))

    
ans.reverse()

for a in ans:
    print(a)