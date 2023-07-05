from collections import deque
INF = 10 ** 18



N, M = map(int, input().split())

G = [set() for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: int(x)-1, input().split())
    G[u].add(v)
    G[v].add(u)

K = int(input())
Q = []

G2 = [set() for _ in range(N)]
white_v = set()
colors = [-1] * N
p_set = set()
for i in range(K):
    p, d = map(int, input().split())
    p -= 1
    p_set.add(p)


    if d == 0:
        G2[p].add(p)
    else:
        que = deque([p])
        dist = [INF] * N
        dist[p] = 0
        white_v.add(p)
        while len(que):
            v = que.popleft()
            for nv in G[v]:
                if dist[v] + 1 >= dist[nv]: continue
                dist[nv] = dist[v] + 1
                if dist[nv] == d:
                    G2[p].add(nv)
                    continue
                white_v.add(nv)
                que.append(nv)

if len(white_v) == N:
    print("No")
    exit()

for g in G2:
    if len(g) == 0: continue
    cnt = 0
    for p in g:
        if p in white_v:
            cnt += 1
    if cnt == len(g):
        print("No")
        exit()

ans = []
for i in range(N):
    if i in white_v:
        ans.append("0")
    else:
        ans.append("1")

print("Yes")
print("".join(ans))
