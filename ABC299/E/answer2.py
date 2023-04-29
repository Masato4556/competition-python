from collections import deque
INF = 10 ** 18

def fill(p, d, G, colors):
    if d == 0:
        if colors[p] == 0:
            return False # 白でしか塗りつぶせない頂点に黒を塗る必要があるのでNo
        colors[p] == 1
    else:
        que = deque([p])
        dist = [INF] * len(G)
        dist[p] = 0
        while len(que):
            v = que.popleft()
            if colors[v] == 1:
                return False
            colors[v] = 0
            for next_v in G[v]:
                if dist[v] + 1 >= dist[next_v]: continue
                dist[next_v] = dist[v] + 1

                if dist[next_v] >= d:
                    if colors[next_v] == -1:
                        colors[next_v] = 2
                    continue
                que.append(next_v)

    return True


N, M = map(int, input().split())


G = [set() for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: int(x)-1, input().split())
    G[u].add(v)
    G[v].add(u)

K = int(input())

C = []
colors = [-1] * N
for i in range(K):
    p, d = map(int, input().split())
    p -= 1
    C.append((p, d))
    if not fill(p, d, G, colors):
        print("No")
        exit()

for i in range(N):
    if colors[i] == -1:
        colors[i] = 1
    if colors[i] == 2:
        colors[i] = 1

if 1 not in colors:
    print("No")
    exit()



print("Yes")
print("".join(map(str, colors)))