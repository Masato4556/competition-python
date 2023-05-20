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

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.root(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


def binary_search(arr, target):
    """
    arr: 昇順または降順にソートされた数値の列（リストや配列など）
    target: 探索する数値
    """
    left, right = 0, len(arr) - 1  # 探索範囲の左端と右端
    while left <= right:
        mid = (left + right) // 2  # 探索範囲の中央のインデックス
        if arr[mid] == target:
            return mid  # 探索対象が見つかった場合、そのインデックスを返す
        elif arr[mid] < target:
            left = mid + 1  # 中央より大きい場合、探索範囲を中央より右側にする
        else:
            right = mid - 1  # 中央より小さい場合、探索範囲を中央より左側にする

    # arr中にxが含まれない場合
    # 探索した値と最も近い要素のインデックスを返す
    if left > len(arr) - 1:
        return len(arr) - 1
    elif right < 0:
        return 0
    else:
        if target - arr[right] < arr[left] - target:
            return right
        else:
            return left
