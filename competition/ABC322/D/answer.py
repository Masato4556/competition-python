import numpy as np
from itertools import product


def trim_rows(mino):
    trimming_rows = set()
    for i in range(mino.shape[0]):
        if not np.all(mino[i, :] == "."):
            break
        trimming_rows.add(i)
    for i in range(mino.shape[0]-1, -1, -1):
        if not np.all(mino[i, :] == "."):
            break
        trimming_rows.add(i)

    return np.delete(mino, list(trimming_rows), 0)


def trim_columns(mino):
    trimming_columns = set()
    for i in range(mino.shape[1]):
        if not np.all(mino[:, i] == "."):
            break
        trimming_columns.add(i)
    for i in range(mino.shape[1]-1, -1, -1):
        if not np.all(mino[:, i] == "."):
            break
        trimming_columns.add(i)

    return np.delete(mino, list(trimming_columns), 1)


def trim_mino(mino):
    return trim_columns(trim_rows(mino))


class Grid:
    def __init__(self):
        self.grid = np.zeros((4, 4))
        self.success = True

    def fill(self, mino, up, left):
        for x in range(mino.shape[0]):
            for y in range(mino.shape[1]):
                if mino[x, y] == "#":
                    self.grid[up+x, left+y] += 1

    def isFilledAll(self):
        return np.all(self.grid == 1)


a_mino = trim_mino(np.array([list(input()) for _ in range(4)]))
b_mino = trim_mino(np.array([list(input()) for _ in range(4)]))
c_mino = trim_mino(np.array([list(input()) for _ in range(4)]))

block_count = 0
block_count += np.count_nonzero(a_mino == "#")
block_count += np.count_nonzero(b_mino == "#")
block_count += np.count_nonzero(c_mino == "#")
if block_count != 16:
    print("No")
    exit()

# 全探索
for ar in range(4):
    rotated_a_mino = np.rot90(a_mino, ar)
    for ax, ay in product(range(5 - rotated_a_mino.shape[0]), range(5 - rotated_a_mino.shape[1])):
        for br in range(4):
            rotated_b_mino = np.rot90(b_mino, br)
            for bx, by in product(range(5 - rotated_b_mino.shape[0]), range(5 - rotated_b_mino.shape[1])):
                for cr in range(4):
                    rotated_c_mino = np.rot90(c_mino, cr)
                    for cx, cy in product(range(5 - rotated_c_mino.shape[0]), range(5 - rotated_c_mino.shape[1])):
                        g = Grid()
                        g.fill(rotated_a_mino, ax, ay)
                        g.fill(rotated_b_mino, bx, by)
                        g.fill(rotated_c_mino, cx, cy)
                        if g.isFilledAll():
                            print("Yes")
                            exit()

print("No")
