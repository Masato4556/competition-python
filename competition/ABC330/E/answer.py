import heapq
from collections import Counter


class LazyHeap:
    def __init__(self, arr=[]):
        self.que = arr.copy()
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


N, Q = map(int, input().split())
A = list(map(int, input().split()))

counter = Counter(A)

heap = LazyHeap([])
for i in range(N+1):
    if counter[i] == 0:
        heap.push(i)

# print(heap)

for _ in range(Q):
    i, x = map(int, input().split())
    i -= 1

    prev_x = A[i]
    counter[prev_x] -= 1
    if counter[prev_x] == 0:
        heap.push(prev_x)

    if counter[x] == 0:
        heap.erase(x)
    counter[x] += 1
    A[i] = x

    # print(heap)

    ans = heap.pop()
    print(ans)
    heap.push(ans)
