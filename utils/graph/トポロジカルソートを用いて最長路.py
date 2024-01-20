# ABC335_Eで用いた
from collections import deque

N, M = map(int, input().split())

G = [set() for _ in range(N)]
indeg = [0] * N
for _ in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())

    G[u].add(v)
    indeg[v] += 1  # 入次数のカウント


que = deque()
dist = [0] * N
dist[0] = 1

# 入次数が0のノードをキューに詰める
for i in range(N):
    if indeg[i] == 0:
        que.append(i)

while que:
    v = que.popleft()
    for next_v in G[v]:
        indeg[next_v] -= 1
        if indeg[next_v] == 0:
            que.append(next_v)
        if dist[v] == 0:
            continue
        if dist[next_v] < dist[v] + 1:
            dist[next_v] = dist[v] + 1

print(dist)
