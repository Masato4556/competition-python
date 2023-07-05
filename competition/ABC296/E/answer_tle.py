from collections import deque

N = int(input())

A = list(map(int, input().split()))

G = [-1 for _ in range(N+1)]

for i in range(1, N+1):
    G[i] = A[i-1]

loop = set()
for i in range(1, N+1):
    if i in loop: continue
    visited = set()
    que = deque([i])

    path = [-1] * (N + 1)

    prev_v = -1

    while que:
        v = que.popleft()
        path[v] = prev_v

        if v in visited:
            vv = v
            while vv not in loop:
                loop.add(vv)
                path[vv]
            break
        visited.add(v)
        prev_v = v
        que.append(G[v])

print(len(loop))
