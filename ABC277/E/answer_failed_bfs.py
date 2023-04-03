from collections import deque

INF = 10**18

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

dist = [INF] * (2 * N)
dist[0] = 0
que = deque([0])


while len(que):
    v = que.popleft()

    for next_v in G[v]:
        d = 0 if abs(next_v - v) == N else 1
        if dist[v] + d >= dist[next_v]: continue
        dist[next_v] = dist[v] + d
        que.append(next_v)

ans = min(dist[N-1], dist[-1])
if ans == INF:
    print(-1)
else:
    print(ans)

