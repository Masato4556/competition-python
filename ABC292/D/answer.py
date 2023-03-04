from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n
        self.edge_count = [0] * n

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
        if rx == ry:
            self.edge_count[rx] += 1
            return False
        # union by rank
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.par[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry]
        self.edge_count[rx] += self.edge_count[ry]
        self.edge_count[rx] += 1
        return True

    def size(self, x):
        return self.siz[self.root(x)]

    def edge_size(self, x):
        return self.edge_count[self.root(x)]

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.root(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

n, m = map(int, input().split())
G = [[] for _ in range(n)]

uf = UnionFind(n)
edge_count = defaultdict(int)

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    uf.unite(u, v)

for root in uf.all_group_members().keys():
    if uf.size(root) != uf.edge_size(root):
        print("No")
        exit()
print("Yes")
