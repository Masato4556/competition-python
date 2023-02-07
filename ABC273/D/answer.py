from collections import defaultdict
from functools import lru_cache

@lru_cache(None)
def input2query(inp):
    d, l = inp.split()
    return (d, int(l))

h, w, rs, cs = map(int, input().split())
n = int(input())
walls_x, walls_y = defaultdict(list), defaultdict(list)
for _ in range(n):
    y, x = map(int, input().split())
    walls_x[x].append(y)
    walls_y[y].append(x)

@lru_cache(None)
def move(curr_x, curr_y, d, l):
    if d == "U":
        x = curr_x
        y = curr_y - l
        for wall_y in walls_x[x]:
            if y <= wall_y < curr_y:
                y = wall_y + 1
    if d == "D":
        x = curr_x
        y = curr_y + l
        for wall_y in walls_x[x]:
            if curr_y < wall_y <= y:
                y = wall_y - 1
    if d == "L":
        x = curr_x - l
        y = curr_y
        for wall_x in walls_y[y]:
            if x <= wall_x < curr_x:
                x = wall_x + 1
    if d == "R":
        x = curr_x + l
        y = curr_y
        for wall_x in walls_y[y]:
            if curr_x < wall_x <= x:
                x = wall_x - 1

    if x <= 0:
        x = 1
    if x > w:
        x = w
    if y <= 0:
        y = 1
    if y > h:
        y = h

    return (x, y)


q = int(input())
queries = [input2query(input()) for _ in range(q)]

curr_pos = [cs, rs]

for query in queries:
    curr_pos = move(curr_pos[0], curr_pos[1], query[0], query[1])
    print(curr_pos[1], curr_pos[0])