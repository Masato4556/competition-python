import heapq
from collections import deque

N, M, K = map(int, input().split())

INF = 10**18

G = [set() for _ in range(N*2)]

for _ in range(M):
    u, v, a = map(int, input().split())
    u -= 1
    v -= 1
    # print(u + N*a, v + N*a)
    G[u + N*a].add(v + N*a)
    G[v + N*a].add(u + N*a)

S = list(map(lambda x: int(x)-1, input().split()))
for s in S:
    G[s].add(s+N)
    G[s+N].add(s)

# print(G)

# que = [(0, N)]
# dist = [INF] * (2*N)
# dist[N] = 0

# while len(que):
#     d, v = heapq.heappop(que)
#     # print(v)

#     for next_v in G[v]:
#         if dist[next_v] != INF:
#             continue
#         next_dist = dist[v] if abs(v - next_v) == N else dist[v] + 1
#         dist[next_v] = min(dist[next_v], next_dist)
#         heapq.heappush(que, (dist[next_v], next_v))

# ans = min(dist[N-1], dist[2*N-1])
# # print(dist)
# print(-1 if ans == INF else ans)


def bfs_dist(graph, start):
    # 各ノードについて、そこまでの最短経路の長さを保持するための辞書
    dist = [-1] * len(graph)
    # キューに開始ノードを追加する
    queue = deque([start])
    dist[start] = 0

    while queue:
        v = queue.popleft()
        for next_v in graph[v]:
            if dist[next_v] != -1:
                continue
            dist[next_v] = dist[v] + 1
            queue.append(next_v)

    return dist


dist = bfs_dist(G, N)

print(dist)
