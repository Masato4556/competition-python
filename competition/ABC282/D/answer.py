from collections import deque

N, M = map(int, input().split())
G = [set() for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: int(x)-1, input().split())
    G[u].add(v)
    G[v].add(u)

colors = [-1] * N

ans = 0
for i in range(N):
    if colors[i] != -1:
        continue

    que = deque([i])
    colors[i] = 0
    nodes = []
    cnt = [0, 0]
    while len(que):
        v = que.popleft()
        nodes.append(v)
        cnt[colors[v]] += 1

        for next_v in G[v]:
            if colors[next_v] != -1:
                if colors[next_v] == colors[v]:
                    print(0)
                    exit()
                continue

            colors[next_v] = 1 if colors[v] == 0 else 0
            que.append(next_v)

    for u in nodes:
        ans += N - cnt[colors[u]] - len(G[u])

print(ans//2)
