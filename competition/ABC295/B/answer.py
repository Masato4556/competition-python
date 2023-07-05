# map
R, C = map(int, input().split())

B = [list(input()) for _ in range(R)]

def dfs(i, j, l, cnt):
    if not (0 <= i < R and 0 <= j < C): return
    if cnt > l: return

    if B[i][j] == "#" or cnt == 0:
        B[i][j] = '.'

    dfs(i-1, j, l, cnt+1)
    dfs(i+1, j, l, cnt+1)
    dfs(i, j-1, l, cnt+1)
    dfs(i, j+1, l, cnt+1)

for i in range(R):
    for j in range(C):
        if B[i][j] not in ("#", "."):
            dfs(i, j, int(B[i][j]), 0)

for b in B:
    print("".join(b))