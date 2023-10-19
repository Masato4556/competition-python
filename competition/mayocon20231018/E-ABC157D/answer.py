from collections import defaultdict


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

    def all_group_members(self): # 
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.root(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

N, M, K = map(int, input().split())

uf = UnionFind(N)
friend_num = [0 for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    friend_num[a] += 1
    friend_num[b] += 1
    uf.unite(a, b)

block_num_in_same_group = [0 for _ in range(N)]
for _ in range(K):
    c, d = map(lambda x: int(x)-1, input().split())
    if uf.issame(c, d):
        block_num_in_same_group[c] += 1
        block_num_in_same_group[d] += 1


print(*[uf.size(i) - friend_num[i] - block_num_in_same_group[i] - 1 for i in range(N)])