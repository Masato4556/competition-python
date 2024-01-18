
from collections import defaultdict
from functools import lru_cache


MOD = 998244353


def moddiv(x, y):
    return (x * modpow(y, MOD-2)) % MOD


@lru_cache(None)
def modpow(x, y):
    return pow(x, y, MOD)


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


H, W = map(int, input().strip().split())
S = [input().strip() for _ in range(H)]


def getInd(h, w):
    return W*h+w


uf = UnionFind(H*W)

for i in range(H):
    for j in range(W):
        if S[i][j] != "#":
            continue

        if i+1 < H and S[i+1][j] == "#":
            uf.unite(getInd(i, j), getInd(i+1, j))

        if j+1 < W and S[i][j+1] == "#":
            uf.unite(getInd(i, j), getInd(i, j+1))

# print(uf)

# green_connected_component_num
gcc_num = sum([1 for i in uf.roots() if S[i // W][i % W] == "#"])
# print("gcc_num", gcc_num)

ans = 0
cnt = 0

for i in range(H):
    for j in range(W):
        if S[i][j] != ".":
            continue

        roots = set()
        if i-1 >= 0 and S[i-1][j] == "#":
            roots.add(uf.root(getInd(i-1, j)))
            # print("D")
        if i+1 < H and S[i+1][j] == "#":
            roots.add(uf.root(getInd(i+1, j)))
            # print("U")
        if j-1 >= 0 and S[i][j-1] == "#":
            roots.add(uf.root(getInd(i, j-1)))
            # print("L")
        if j+1 < W and S[i][j+1] == "#":
            roots.add(uf.root(getInd(i, j+1)))
            # print("R")
        # print(i, j, roots)

        if len(roots) == 0:
            # print(gcc_num + 1)
            ans += gcc_num + 1
        elif len(roots) == 1:
            # print(gcc_num)
            ans += gcc_num
        else:
            # print(gcc_num - len(roots) + 1)
            ans += gcc_num - len(roots) + 1
        ans %= 998244353
        cnt += 1

# print(ans, cnt)
print(moddiv(ans, cnt))
