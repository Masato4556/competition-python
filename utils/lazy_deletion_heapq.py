'''
挿入、削除、最小値取得がならし計算量O(logN)で行えるデータ構造

heapify: O(N)
挿入(push): O(logN) ならし計算量
削除(erase): O(logN) ならし計算量
最小値取得(pop): O(logN) ならし計算量

参考: https://socha77.hatenablog.com/entry/2020/06/17/012842
'''

import heapq

class LazyDeletionHeapq:
    def __init__(self, arr=[]):
        self.que = arr
        self.deleted = []

        heapq.heapify(self.que)

    def push(self, x):
        heapq.heappush(self.que, x) 

    def erase(self, x):
        heapq.heappush(self.deleted, x)
        # FIXME: 存在しない要素を消そうとすると壊れる

    def pop(self):
        while self.deleted and self.que[0] == self.deleted[0]:
            heapq.heappop(self.que)
            heapq.heappop(self.deleted)
        return heapq.heappop(self.que)

    def has_next(self):
        while self.que and self.deleted and self.que[0] == self.deleted[0]:
            heapq.heappop(self.que)
            heapq.heappop(self.deleted)

        return len(self.que) > 0
    def __str__(self):
        return str(self.que) + " DELETED: " + str(self.deleted)



ldh = LazyDeletionHeapq([1,6,3,5,9,12,17,12])

print(ldh)
print(ldh.pop())
print(ldh)
ldh.erase(9)
print(ldh)

while ldh.has_next():
    print(ldh.pop())
    print(ldh)