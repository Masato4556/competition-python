import heapq
N, M, K = map(int, input().split())

G = [set() for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: int(x)-1, input().split())
    G[u].add(v)
    G[v].add(u)

hp = [-1] * N
que = []
for _ in range(K):
    p, h = map(int, input().split())
    heapq.heappush(que, (-h, p-1))

while len(que):
    h, v = heapq.heappop(que)
    h *= -1
    if h <= hp[v]:
        continue

    hp[v] = h

    for nv in G[v]:
        heapq.heappush(que, (-(h-1), nv))

ans = [i+1 for i, v in enumerate(hp) if v != -1]
print(len(ans))
print(*ans)
