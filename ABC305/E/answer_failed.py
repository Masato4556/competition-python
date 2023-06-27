from collections import deque
import heapq
N, M, K = map(int, input().split())

G = [set() for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: int(x)-1, input().split())
    G[u].add(v)
    G[v].add(u)

ans = [0] * N
PH = []
for _ in range(K):
    p, h = map(int, input().split())
    heapq.heappush(PH, (-h, p))

for _ in range(K):
    h, p = heapq.heappop(PH)
    h *= -1
    p -= 1

    que = deque([(p, h)])
    ans[p] = 1

    reach = [-1] * N
    while len(que):
        v, ch = que.popleft()
        if ch <= reach[v]:
            continue

        reach[v] = ch
        ans[v] = 1
        # print(v, ch, reach[v], reach)

        for nv in G[v]:
            if reach[nv] != -1:
                continue

            que.append((nv, ch-1))

print(ans.count(1))
print(*[i+1 for i, v in enumerate(ans) if v == 1])
