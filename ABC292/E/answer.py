from collections import deque

n, m = map(int, input().split())
G = [set() for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].add(v)

seens = [set() for _ in range(n)]

for i in range(n):
    que = deque([i])

    while len(que):
        v = que.popleft()
        for next_v in G[v]:
            if next_v in seens[i]: continue
            if next_v == i : continue
            que.append(next_v)
            seens[i].add(next_v)

print(sum([len(seen) for seen in seens]) - sum([len(g) for g in G])  )


