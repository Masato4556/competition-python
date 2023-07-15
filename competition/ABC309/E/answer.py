from collections import deque


def bfs(graph, start, Y):
    dist = [-1] * len(graph)
    dist[start] = 0
    queue = deque([start])

    while queue:
        v = queue.popleft()
        for nv in graph[v]:
            if dist[nv] != -1:
                continue
            Y[nv] = max(Y[nv], Y[v] - 1)
            dist[nv] = dist[v] + 1
            queue.append(nv)


N, M = map(int, input().split())
P = list(map(lambda x: int(x)-1, input().split()))

G = [set() for _ in range(N)]
for i in range(1, N):
    G[P[i-1]].add(i)

Y = [-1] * N

for _ in range(M):
    x, y = map(int, input().split())
    x -= 1

    Y[x] = max(Y[x], y)

# print(G)
# print(Y)
bfs(G, 0, Y)
# print(Y)

print(len([i+1 for i, v in enumerate(Y) if v >= 0]))
