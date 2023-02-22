
from collections import defaultdict, deque
n = int(input())

ToIndex = dict()
G = [[] for _ in range(n)]

C = [
    (-1,-1),
    (-1,0),
    (0,-1),
    (0,1),
    (1,0),
    (1,1),
]

ind = 0
for _ in range(n):
    x, y = map(int, input().split())
    if (x, y) not in ToIndex: 
            ToIndex[(x, y)] = ind
            ind += 1
    for x_offset, y_offset in C:
        if (x + x_offset, y + y_offset) not in ToIndex: continue

        G[ToIndex[(x, y)]].append(ToIndex[(x + x_offset, y + y_offset)])
        G[ToIndex[(x + x_offset, y + y_offset)]].append(ToIndex[(x, y)])

seen = [False for _ in range(n)]
ans = 0

while False in seen:
    ans += 1
    que = deque([seen.index(False)])
    while len(que):
        v = que.popleft()
        seen[v] = True

        for next_v in G[v]:
            if seen[next_v]: continue
            seen[next_v] = True
            que.append(next_v)

print(ans)