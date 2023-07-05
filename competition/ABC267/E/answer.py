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

N, M = map(int, input().split())
A = list(map(int, input().split()))

costs = [0] * N
G = [set() for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x:int(x) - 1, input().split())
    G[u].add(v)
    G[v].add(u)
    costs[u] += A[v]
    costs[v] += A[u]

que = LazyDeletionHeapq()

for i in range(N):
    que.push((costs[i], i))

deleted = set()

ans = 0
while que.has_next():
    cost, v = que.pop()
    deleted.add(v)
    ans = max(ans, cost)
    for next_v in G[v]:
        if next_v in deleted: continue
        que.erase((costs[next_v], next_v))
        costs[next_v] -= A[v]
        que.push((costs[next_v], next_v))

print(ans)

