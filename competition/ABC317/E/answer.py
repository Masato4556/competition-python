from collections import deque

H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]

objective_char = set(["#", ">", "v", "<", "^"])

for y in range(H):
    for x in range(W):
        if A[y][x] == 'S':
            start = (x, y)
            continue
        if A[y][x] == 'G':
            goal = (x, y)
            continue

        dx = 0
        dy = 0
        if A[y][x] == '>':
            dx = 1
        elif A[y][x] == '<':
            dx = -1
        elif A[y][x] == 'v':
            dy = 1
        elif A[y][x] == '^':
            dy = -1
        else:
            continue
        nx = x + dx
        ny = y + dy
        while 0 <= nx < W and 0 <= ny < H:
            if A[ny][nx] in objective_char:
                break
            A[ny][nx] = "*"
            nx += dx
            ny += dy

que = deque([start])
dist = viewed = [[-1] * W for _ in range(H)]
dist[start[1]][start[0]] = 0

while len(que):
    x, y = que.popleft()

    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        if not (0 <= x + dx < W and 0 <= y + dy < H):
            continue
        if dist[y+dy][x+dx] != -1:
            continue
        if A[y+dy][x+dx] in objective_char or A[y+dy][x+dx] == "*":
            continue
        dist[y+dy][x+dx] = dist[y][x] + 1
        que.append((x+dx, y+dy))

print(dist[goal[1]][goal[0]])
