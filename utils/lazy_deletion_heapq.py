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

    def __str__(self):
        return str(self.que) + " DELETED: " + str(self.deleted)

    def __len__(self):
        return len(self.que) - len(self.deleted)


ldh = LazyDeletionHeapq([1,6,3,5,9,12,17,12])

print(ldh, len(ldh))
print(ldh.pop())
print(ldh, len(ldh))
ldh.erase(9)
print(ldh, len(ldh))

while len(ldh):
    print(ldh.pop())
    print(ldh, len(ldh))