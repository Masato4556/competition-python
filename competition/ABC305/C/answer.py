
H, W = map(int, input().split())

S = [input() for _ in range(H)]


min_x = W
max_x = 0
min_y = H
max_y = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            min_x = min(min_x, j)
            max_x = max(max_x, j)
            min_y = min(min_y, i)
            max_y = max(max_y, i)


for i in range(min_y, max_y+1):
    for j in range(min_x, max_x+1):
        if S[i][j] == ".":
            print(f"{i+1} {j+1}")
            exit()
