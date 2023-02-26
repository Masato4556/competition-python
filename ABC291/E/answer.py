from collections import deque

def f(G, deg):
    que = deque([])

    for v in range(n):
        if deg[v] == 0:
            que.append(v)

    order = []

    while len(que) > 0:
        v = que.popleft()
        order.append(v)

        for v2 in G[v]:
            deg[v2] -= 1
            if deg[v2] == 0: que.append(v2)
    return order

n, m = map(int, input().split())
G = [[] for _ in range(n)]
deg = [0 for _ in  range(n)]
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if x in G[y]: continue

    G[y].append(x)
    deg[x] += 1

for i in range(n):
    G[i].sort(reverse=True)

order = f(G, deg.copy())

if all([d < 2 for d in deg]) and len([d for d in deg if d == 0]) == 1:
    print('Yes')
    c = {v:i+1 for i, v in enumerate(reversed(order))}
    print(*[c[i] for i in range(n)])
else:
    print('No')