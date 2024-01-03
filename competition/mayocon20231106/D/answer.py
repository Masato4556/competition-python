def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    g = gcd(a, b)
    return a // g * b


def segfunc(x, y):
    return gcd(x, y)


class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.leaf_num = 1 << (n-1).bit_length()
        self.tree = [ide_ele]*2*self.leaf_num  # インデックス0は利用せず、1以降のみを用いる

        # 葉ノードの初期化
        for i in range(n):
            self.tree[self.leaf_num+i] = init_val[i]
        # 葉ノード以外の初期化
        for i in range(self.leaf_num-1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])

    def add(self, ind, x):
        ind += self.leaf_num
        self.tree[ind] += x
        while ind > 1:
            self.tree[ind >> 1] = self.segfunc(
                self.tree[ind], self.tree[ind ^ 1])
            ind >>= 1

    def update(self, ind, x):
        ind += self.leaf_num
        self.tree[ind] = x
        while ind > 1:
            self.tree[ind >> 1] = self.segfunc(
                self.tree[ind], self.tree[ind ^ 1])
            ind >>= 1

    def query(self, left, right):
        # [left, right)の区間の計算結果を返す　
        # 全区間の計算結果を取得したいなら[0, N)
        # [i, i)の場合、区間が存在しないためide_eleを返す
        res = self.ide_ele
        left += self.leaf_num
        right += self.leaf_num
        while left < right:
            if left & 1:
                res = self.segfunc(res, self.tree[left])
                left += 1
            if right & 1:
                res = self.segfunc(res, self.tree[right-1])
            left >>= 1
            right >>= 1
        return res


N = int(input())
A = list(map(int, input().split()))

ide_ele = 1
for a in A:
    ide_ele = lcm(ide_ele, a)

segtree = SegTree(A, segfunc, ide_ele)
print(max([gcd(segtree.query(0, i), segtree.query(i+1, N)) for i in range(N)]))
