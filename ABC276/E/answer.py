# TODO union findで解く方法を試す
# Sの上下左右のマスのうちの２つが、同じグループに属していれば”Yes”

from queue import Queue
from  itertools import combinations

h, w = map(int, input().split())
C = [input() for _ in range(h)]

G = [[[] for _ in range(w)] for _ in range(h)]
base_pos = (0, 0)
offsets = [(0, 1), (0, -1), (1, 0), (-1,0)]
for y in range(h):
    for x in range(w):
        if C[y][x] == "#": continue
        if C[y][x] == "S": base_pos = (x, y)
        for offset_x, offset_y in offsets:
            next_x = x + offset_x
            next_y = y + offset_y
            if next_x < 0 or w <= next_x: continue
            if next_y < 0 or h <= next_y: continue
            if C[next_y][next_x] == "#": continue
            G[y][x].append((next_x, next_y))

result = "No"
for s_offset, e_offset in combinations(offsets, 2):
    s_x, s_y = base_pos[0]+s_offset[0], base_pos[1]+s_offset[1]
    e_x, e_y = base_pos[0]+e_offset[0], base_pos[1]+e_offset[1]

    if result == "Yes": break
    if C[s_y][s_x] == "#": continue
    if C[e_y][e_x] == "#": continue

    que = Queue()
    que.put((s_x, s_y))
    seen = [[False for _ in range(w)] for _ in range(h)]
    seen[base_pos[1]][base_pos[0]] = True
    
    while not que.empty():
        x, y = que.get()

        seen[y][x] = True

        for next_x, next_y in G[y][x]:
            if seen[next_y][next_x]: continue
            if next_x == e_x and next_y == e_y:
                result = "Yes"
                break 
            que.put((next_x, next_y))


print(result)