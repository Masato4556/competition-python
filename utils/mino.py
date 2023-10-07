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


# 活用例　ABC322D
