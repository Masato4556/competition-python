from collections import deque


def bfs(graph, start):
    dist = [-1] * len(graph)
    dist[start] = 0
    queue = deque([start])

    while queue:
        v = queue.popleft()
        for nv in graph[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            queue.append(nv)

    return dist


N1, N2, M = map(int, input().split())

G = [set() for _ in range(N1+N2)]
for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    G[a].add(b)
    G[b].add(a)

print(max(bfs(G, 0)) + max(bfs(G, N1+N2-1)) + 1)
