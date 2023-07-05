from  itertools import combinations
from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    def root(self, x):
        try:
            if self.par[x] == -1: return x
        except IndexError as e:
            print(x, e)

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


h, w = map(int, input().split())
C = [input() for _ in range(h)]

def calc_index(x, y):
    return y*w + x

def is_valid_pos(x, y):
    if x < 0 or w <= x: return False
    if y < 0 or h <= y: return False
    return True

uf = UnionFind(h * w)

base_pos = (0, 0)
offsets = [(0, 1), (0, -1), (1, 0), (-1,0)]
for y in range(h):
    for x in range(w):
        if C[y][x] == "#": continue
        if C[y][x] == "S": 
            base_pos = (x, y)
            continue
        for offset_x, offset_y in offsets:
            next_x = x + offset_x
            next_y = y + offset_y
            if not is_valid_pos(next_x, next_y): continue
            if C[next_y][next_x] in ("#", "S"): continue
            uf.unite(calc_index(x, y), calc_index(next_x, next_y))

result = "No"
for s_offset, e_offset in combinations(offsets, 2):
    s_x, s_y = base_pos[0]+s_offset[0], base_pos[1]+s_offset[1]
    e_x, e_y = base_pos[0]+e_offset[0], base_pos[1]+e_offset[1]

    if not is_valid_pos(s_x, s_y): continue
    if not is_valid_pos(e_x, e_y): continue

    if uf.issame(calc_index(s_x, s_y), calc_index(e_x, e_y)):
        result = "Yes"
        break

print(result)