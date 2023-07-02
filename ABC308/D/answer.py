from collections import deque
H, W = map(int, input().split())

S = [input() for _ in range(H)]

next_char = {
    "s": "n",
    "n": "u",
    "u": "k",
    "k": "e",
    "e": "s",
}

offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]

que = deque([(0, 0)])

seen = [[0 for _ in range(W)] for _ in range(H)]
seen[0][0] = 1

if S[0][0] != "s":
    print("No")
    exit()

while len(que):
    i, j = que.popleft()

    if not S[i][j] in next_char:
        continue

    for add_i, add_j in offsets:
        if not (0 <= i+add_i < H and 0 <= j+add_j < W):
            continue
        if seen[i+add_i][j+add_j]:
            continue
        if S[i+add_i][j+add_j] == next_char[S[i][j]]:
            que.append((i+add_i, j+add_j))
            seen[i+add_i][j+add_j] = 1

print("Yes" if seen[-1][-1] else "No")
