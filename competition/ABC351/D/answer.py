from collections import deque
from collections import defaultdict
import pprint
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


H, W = MAP(int)
S = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            if i - 1 >= 0 and S[i-1][j] == ".":
                S[i-1][j] = "o"
            if i + 1 < H and S[i+1][j] == ".":
                S[i+1][j] = "o"
            if j - 1 >= 0 and S[i][j-1] == ".":
                S[i][j-1] = "o"
            if j + 1 < W and S[i][j+1] == ".":
                S[i][j+1] = "o"


uf = UnionFind(H*W)

ans = 1
visited = set()
for x in range(H):
    for y in range(W):
        if S[x][y] != '.':
            continue

        cur_visited = set()
        visited.add((x, y))

        queue = deque([(x, y)])
        count = 1

        while queue:
            i, j = queue.popleft()

            for diff in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = i + diff[0], j + diff[1]
                if 0 <= nx < H and 0 <= ny < W:
                    if (nx, ny) in visited or (nx, ny) in cur_visited:
                        continue
                    if S[nx][ny] == ".":
                        visited.add((nx, ny))
                        count += 1
                        queue.append((nx, ny))
                        continue
                    if S[nx][ny] == "o":
                        cur_visited.add((nx, ny))
                        count += 1
        ans = max(ans, count)

print(ans)
