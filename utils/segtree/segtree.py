# 参考ページ: https://qiita.com/ether2420/items/7b67b2b35ad5f441d686

# 右のページを読んで理解する https://qiita.com/AkariLuminous/items/32cbf5bc3ffb2f84a898
# initまでは理解した、次はadd

def segfunc(x, y):
    return x+y


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

    def query(self, left, right):  # [left, right)の区間の計算結果を返す
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


a = SegTree([1, 2, 3, 4, 5, 6, 7, 8], segfunc, 0)
print(a.tree)  # インデックス0は使われていない
print(a.query(3, 7))
