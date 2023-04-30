

H, W = map(int, input().split())
C = [input() for _ in range(H)]

def check(x, y, d):
    global C, H, W
    for offset_x, offset_y in ((0, 0),(1, 1),(1, -1),(-1, 1),(-1, -1)):
        if not (0 <= x+ offset_x*d < H and 0 <= y+ offset_y*d < W): return False
        if C[x+ offset_x*d][y+ offset_y*d] != "#": return False
    return True

ans = [0] * min(H, W)
n = min(H, W)

for x in range(1, H-1):
    for y in range(1, W-1):
        cnt = 0
        for d in range(1, n):
            if not check(x, y, d): break
            cnt += 1
        if cnt > 0:
            ans[cnt-1] += 1

print(" ".join(map(str, ans)))