from collections import deque
import heapq

INF = float('inf')

def dijkstra(N, adj_list, start):
    dist = [INF] * (2*N)
    dist[start] = 0
    heap = [(0, start)]
    heapq.heapify(heap)

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v in adj_list[u]:
            d = 0 if abs(u - v) == N else 1 # スイッチを押すときは移動としてカウントしない
            if dist[v] > dist[u] + d:
                dist[v] = dist[u] + d
                heapq.heappush(heap, (dist[v], v))

    return dist



N, M, K = map(int, input().split())

# 0~N-1は奇数回スイッチを押した時のノード、N~2N-1は偶数回スイッチを押した時のノード
G = [set() for _ in range(2*N)]
for _ in range(M):
    u, v, a = map(int, input().split())
    u -= 1
    v -= 1
    if a == 0:
        u += N
        v += N
    G[u].add(v)
    G[v].add(u)

for u in map(lambda x: int(x)-1, input().split()):
    v = u + N 
    G[u].add(v)
    G[v].add(u)

dist = dijkstra(N, G, 0)
ans = min(dist[N-1], dist[-1])
print(ans if ans != INF else -1)
