from collections import deque

N, M = map(int, input().split())

G = [[] for _ in range(N)]

for _ in range(M):
    a, b, x, y = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append((b, x, y))
    G[b].append((a, -x, -y))

# print(G)

decidable = [False for _ in range(N)]
positions = [[0, 0] for _ in range(N)]
decidable[0] = True

que = deque([0])
while len(que):
    v = que.popleft()

    for next_v, x, y in G[v]:
        if decidable[next_v]:
            continue
        positions[next_v][0] = positions[v][0] + x
        positions[next_v][1] = positions[v][1] + y
        decidable[next_v] = True
        que.append(next_v)

# print(decidable)
# print(positions)

for i in range(N):
    if decidable[i]:
        print(*positions[i])
    else:
        print("undecidable")
