
h, w = map(int, input().split())
G = []
for _ in range(h):
    G.append(input())

seen = set()
pos = (0, 0)

c = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

ans = -1
while pos not in seen:
    seen.add(pos)
    move = c[G[pos[0]][pos[1]]]
    if not (0 <= pos[0] + move[0] < h and 0 <= pos[1] + move[1] < w):
        print(pos[0]+1, pos[1]+1)
        exit()
    pos = (pos[0] + move[0], pos[1] + move[1])
        
print(-1)

