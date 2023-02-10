from collections import deque

def validPos(x, y, n):
    return True if 0 <= x < n and 0 <= y < n else False

n, m = map(int, input().split())

result = [[-1 for _ in range(n)] for _ in range(n)]
result[0][0] = 0
move = []

k = 0
while k * k <= m:
    m2 = m - k * k
    l = 0
    while l * l <= m2:
        if l * l == m2: 
            move.extend([(k, l), (k, -l), (-k, l), (-k, -l)])
        l += 1
    k += 1

que = deque([(0, 0)])
while len(que) > 0:
    x, y = que.popleft()

    for k, l in move:
        if not validPos(x+k, y+l, n): continue
        if result[y][x] + 1 >= result[y+l][x+k] and result[y+l][x+k] != -1: continue

        result[y+l][x+k] = result[y][x] + 1
        que.append((x+k, y+l))

for r in result:
    print(*r)
