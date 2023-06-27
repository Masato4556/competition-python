from collections import deque
from math import sqrt

N, D = map(int, input().split())

pos = [tuple(map(int, input().split())) for _ in range(N)]

G = [set() for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        if sqrt((pos[i][0] - pos[j][0])**2 + (pos[i][1] - pos[j][1])**2) <= D:
            G[i].add(j)
            G[j].add(i)

que = deque([0])
infected = [0] * N
infected[0] = 1

while len(que):
    v = que.popleft()

    for next_v in G[v]:
        if infected[next_v] == 1:
            continue

        infected[next_v] = 1
        que.append(next_v)

for i in range(N):
    print("Yes" if infected[i] else "No")
