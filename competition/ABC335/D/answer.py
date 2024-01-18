from collections import deque
N = int(input())

G = [[0 for _ in range(N)] for _ in range(N)]

G[N//2][N//2] = "T"

next_direction = {
    "R": "D",
    "D": "L",
    "L": "U",
    "U": "R"
}

move = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (1, 0),
    "D": (-1, -0),
}

dist = []
for i in range(45):
    dist.append(i+1)
    dist.append(i+1)

dist_que = deque(dist)

cnt = 1
pos = [N//2, N//2]
direction = "U"
dist = 0
while cnt < N**2:
    if dist == 0:
        direction = next_direction[direction]
        dist = dist_que.popleft()
    pos[0] += move[direction][0]
    pos[1] += move[direction][1]
    G[pos[0]][pos[1]] = cnt

    cnt += 1
    dist -= 1


for row in G:
    print(*row)
