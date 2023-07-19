
import heapq
from collections import Counter


class LazyDeletionHeapq:
    def __init__(self, arr=[]):
        self.que = arr
        self.deleted = []
        self.counter = Counter(arr)

        heapq.heapify(self.que)

    def push(self, x):
        heapq.heappush(self.que, x)
        self.counter[x] += 1

    def erase(self, x):
        if self.counter[x] > 0:
            self.__reserveDeletion(x)

    def pop(self):
        self.__delete()
        return self.__pop()

    def head(self):
        return self.que[0]

    def has_next(self):
        self.__delete()
        return len(self.que) > 0

    def __pop(self):
        ret = heapq.heappop(self.que)
        self.counter[ret] -= 1
        return ret

    def __reserveDeletion(self, x):
        heapq.heappush(self.deleted, x)
        self.counter[x] -= 1

    def __delete(self):
        while self.que and self.deleted and self.que[0] == self.deleted[0]:
            heapq.heappop(self.que)
            heapq.heappop(self.deleted)

    def __len__(self):
        return len(self.que) - len(self.deleted)

    def __str__(self):
        return f"{str(self.que)} DELETED:{str(self.deleted)} LENGTH: {len(self)}, LENGTH: {sum(self.counter.values())}"


# ある数列の大きい順にK個の要素の合計を求めることもできるデータ構造
# 入れる値を-1すれば、小さい順にK個の要素の合計を求めることもできる
class MaxKSum:
    def __init__(self, k, arr=[]):
        self.k = k
        self.que_notk = LazyDeletionHeapq([-1 * v for v in arr])  # 降順
        self.que_k = LazyDeletionHeapq()  # 昇順

        self.total = 0
        self.__balance()

    def push(self, x):
        if x > self.que_k.head():
            if len(self.que_k) == self.k:
                v = self.que_k.pop()
                self.que_notk.push(-1 * v)
                self.total -= v
            self.que_k.push(x)
            self.total += x
        else:
            self.que_notk.push(-1 * x)

    def erase(self, x):
        if x >= self.que_k.head():
            prev_len = len(self.que_k)
            self.que_k.erase(x)
            if prev_len != len(self.que_k):
                self.total -= x
            self.__balance()
        else:
            self.que_notk.erase(-1 * x)

    def getTotal(self):
        return self.total

    def __balance(self):
        while len(self.que_k) < self.k:
            v = -1 * self.que_notk.pop()
            self.que_k.push(v)
            self.total += v


mks = MaxKSum(2, [1, 6, 3, 5, 9, 12, 17, 12])

print(mks.getTotal())
mks.erase(12)  # 要素を削除できる
print(mks.getTotal())
mks.erase(12)  # 要素を削除できる
print(mks.getTotal())
mks.erase(999)  # 存在しない要素を削除しようとしても破綻しない
print(mks.getTotal())

'''
できないこと
- 最小の値をポップする
'''

# ABC306Eで試しに動かしてみたが落ちた。
# ABC306EでACするように修正する
