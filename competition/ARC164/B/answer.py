from collections import deque
N, M = map(int, input().split())

G = [set() for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    G[a].add(b)
    G[b].add(a)

C = list(map(int, input().split()))


checked = set()
for i in range(N):
    if i in checked:
        continue

    que = deque([i])
    visited = set()
    visited.add(i)

    while len(que):
        v = que.pop()
        visited.add(v)
        checked.add(v)

        for nv in G[v]:
            if nv in visited:
                if C[nv] == C[v]:
                    print("Yes")
                    exit()
                continue
            if C[nv] != C[v]:
                que.append(nv)
            
print("No")
            


    



