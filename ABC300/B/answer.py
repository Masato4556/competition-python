
H, W = map(int, input().split())

A = [input() for _ in range(H)]
B = [input() for _ in range(H)]


def f(s, t):
    global A, B, H, W
    for i in range(H):
        for j in range(W):
            if A[i][j] != B[(i+s)%H][(j+t)%W]:
                return False
    return True

for s in range(H):
    for t in range(W):
        if f(s, t):
            print("Yes")
            exit()
print("No")
