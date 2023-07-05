from collections import deque

INF = 10**18

def bfs(graph, start):
    que = deque([start])

    dist = [INF] * len(graph)
    dist[start] = 0
    flg = True

    while que:
        v = que.popleft()
        for next_v in graph[v]:
            if dist[next_v] <= dist[v] + 1: continue
            dist[next_v] = dist[v] + 1

            que.append(next_v)

    return dist

N, K = map(int, input().split())

G = [set() for _ in range(N*2)]
for i in range(N):
    A_row = list(map(int, input().split()))
    for j in range(N):
        if A_row[j]:
            G[i].add(j+N)
            G[i+N].add(j+N)

dists = [bfs(G, i) for i in range(N)]

Q = int(input())

for _ in range(Q):
    s, t = map(lambda x: int(x)-1, input().split())
    print(dists[s%N][t%N + N] if dists[s%N][t%N + N] != INF else -1 )



