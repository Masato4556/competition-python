from collections import deque


n, m = map(int, input().split())
G = [set() for _ in range(n)]
deg = [0] * n

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].add(v)
    deg[u] += 1

ans = 0
targets = [i for i,v in enumerate(deg) if v != 0]
for _ in range(n):
    new_targets = set()
    update = False
    for v in targets:
        A = set()
        new_targets = set()
        for vv in G[v]:
            for vvv in G[vv]:
                if vvv == v: continue
                if vvv in G[v]: continue
                new_targets.add(v)
                A.add((v, vvv))
        for a in A:
            u, v = a
            G[u].add(v)
            update = True
            ans += 1
    target = new_targets
    if not update: break

print(sum([len(g) for g in G]) - m)
