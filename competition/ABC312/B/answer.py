
N, M = map(int, input().split())

S = [input() for _ in range(N)]


def f(i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            if S[x][y] != "#":
                return False
    for x in range(i+6, i+9):
        for y in range(j+6, j+9):
            if S[x][y] != "#":
                return False
    return True


def g(i, j):
    for x in range(i, i+4):
        if S[x][j+3] != ".":
            return False
    for y in range(j, j+4):
        if S[i+3][y] != ".":
            return False
    return True if S[i+3][j+3] == "." else False


ans = []
for i in range(N-8):
    for j in range(M-8):
        if f(i, j) and g(i, j):
            print(i+1, j+1)
