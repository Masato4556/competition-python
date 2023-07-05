from queue import Queue

n, m = map(int, input().split())

G = [[] for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)

que = Queue()
seen = [False] * n
result = 0

while False in seen:
    root = seen.index(False)
    que.put(root)
    seen[root] = True
    result += 1
    while not que.empty():
        v = que.get()
        for next_v in G[v]:
            if seen[next_v]: continue
            que.put(next_v)
            seen[next_v] = True

print(result)


