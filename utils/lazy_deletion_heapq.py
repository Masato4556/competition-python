'''
挿入、削除、最小値取得がならし計算量O(logN)で行えるデータ構造

heapify: O(N)
挿入(push): O(logN) ならし計算量
削除(erase): O(logN) ならし計算量
最小値取得(pop): O(logN) ならし計算量

参考: https://socha77.hatenablog.com/entry/2020/06/17/012842
'''

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


ldh = LazyDeletionHeapq([1, 6, 3, 5, 9, 12, 17, 12])

print(ldh)
print(ldh.pop())  # 最小の要素が取り出せる
print(ldh)
ldh.erase(9)  # 要素の削除が行える(厳密には削除予約ができる)
print(ldh)
ldh.erase(999)  # 存在しない要素を削除しても破綻しない
print(ldh)
while ldh.has_next():
    print(ldh.pop())  # 最小の要素を取り出す際に、削除予定の要素を削除する
    print(ldh)
