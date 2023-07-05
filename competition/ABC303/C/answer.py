N, M, H, K = map(int, input().split())
S = input()
items = set()

for _ in range(M):
    items.add(tuple(map(int, input().split())))

move = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}

pos = [0, 0]
for s in S:
    H -= 1
    if H < 0:
        print("No")
        exit()

    for i in range(2):
        pos[i] += move[s][i]

    if (pos[0], pos[1]) in items and H < K:
        H = K
        items.remove((pos[0], pos[1]))

print("Yes")
