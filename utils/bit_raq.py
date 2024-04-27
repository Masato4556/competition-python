# まだ、理解できていない
# https://qiita.com/toast-uz/items/bf6f142bace86c525532#13-bit

# [l, r]の区間加算と閉区間[1, i]の和の取得を高速軽量に実行できる

# https://algo-logic.info/binary-indexed-tree/#

class BIT_RAQ:
    def __init__(self, n):
        self.n = len(n) if isinstance(n, list) else n
        self.size = 1 << (self.n - 1).bit_length()
        if isinstance(n, list):  # nは1-indexedなリスト
            a = [0]
            for p in n:
                a.append(p + a[-1])
            a += [a[-1]] * (self.size - self.n)
            self.d1 = [a[p] - a[p - (p & -p)] for p in range(self.size + 1)]
        else:                    # nは大きさ
            self.d1 = [0] * (self.size + 1)

        self.d2 = [0] * (self.size + 1)

    def __repr__(self):
        p = self.size
        res = []
        while p > 0:
            res2 = []
            for r in range(p, self.size + 1, p * 2):
                l = r - (r & -r) + 1
                res2.append(f'[{l}, {r}]:{self.d1[r]}')
            res.append(' '.join(res2))
            p >>= 1
        res.append(
            f'{[self.sum(p + 1) - self.sum(p) for p in range(self.size)]}')
        return '\n'.join(res)

    def add(self, p, x):  # O(log(n)), 点pにxを加算
        assert p > 0
        while p <= self.size:
            self.d1[p] += x
            p += p & -p

    def __add_sub(self, p, x):  # O(log(n)), 点pにxを加算
        assert p > 0
        while p <= self.size:
            self.d2[p] += x
            p += p & -p

    def add_range(self, l, r, x):  # O(log(n)), 点pにxを加算
        assert l > 0
        assert r < self.n
        self.add(l, -x * (l-1))
        self.add(r, x * (r-1))
        self.__add_sub(l, x)
        self.__add_sub(r, -x)

    def get(self, p, default=None):     # O(log(n))
        assert p > 0
        return self.sum(p) - self.sum(p - 1) if 1 <= p <= self.n or default is None else default

    def sum(self, p):     # O(log(n)), 閉区間[1, p]の累積和
        assert p >= 0
        res = 0
        while p > 0:
            res += self.d1[p] + self.d2[p] * p
            p -= p & -p
        return res

    def lower_bound(self, x):   # O(log(n)), x <= 閉区間[1, p]の累積和 となる最小のp
        pass  # 未実装


# TODO: きちんと動作するかテスト
