import numpy as np


def trim_rows(mino):
    t = []
    for i in range(4):
        if np.any(a_mino[:, i] == "#"):
            t.append(i)
    dl = []
    print(t)
    next_rows = 0
    for row in t:
        if row != next_rows:
            break
        dl.append(row)
        next_rows += 1
    next_rows = 3
    t.reverse()
    for row in t:
        if row != next_rows:
            break
        dl.append(row)
        next_rows -= 1
    print(dl)
    return np.delete(mino, dl, 0)


def trim_cols(mino):
    t = []
    for i in range(4):
        if np.any(a_mino[:, i] == "#"):
            t.append(i)
    dl = []
    next_rows = 0
    for row in t:
        if row != next_rows:
            break
        dl.append(row)
        next_rows += 1
    next_rows = 3
    t.reverse()
    for row in t:
        if row != next_rows:
            break
        dl.append(row)
        next_rows -= 1

    print(dl)
    return np.delete(mino, dl, 0)


a_mino = np.array([list(input()) for _ in range(4)])
b_mino = np.array([list(input()) for _ in range(4)])
c_mino = np.array([list(input()) for _ in range(4)])
print(a_mino)
# print(np.rot90(a_mino))


print(trim_rows(a_mino))

# print(a_mino[0])
# print(a_mino[:, 0])
