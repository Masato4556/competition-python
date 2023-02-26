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
G3 = [[] for _ in range(n)]
deg = [0 for _ in range(n)]
deg2 = [0 for _ in range(n)]
deg3 = [0 for _ in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    G[x].append(y)
    G3[y].append(x)
    deg[y] += 1
    deg2[y] += 1
    deg3[x] += 1

for i in range(n):
    G[i].sort(reverse=True)

order = f(G, deg)

for i in range(n):
    G[i].sort()

order2 = f(G, deg2)

for i in range(n):
    G3[i].sort(reverse=True)

order3 = f(G3, deg3)


flg = False
for o1, o2 in zip(order, order2):
    if o1 != o2:
        flg = True
        break
if flg:
    print('No')
else:
    print('Yes')
    c = {v:i+1 for i, v in enumerate(reversed(order3))}
    print(*[c[i] for i in range(n)])