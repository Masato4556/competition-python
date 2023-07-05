from collections import deque, defaultdict

N = int(input())

G = defaultdict(set)
for _ in range(N):
    a, b = map(int, input().split())
    G[a].add(b)
    G[b].add(a)

que = deque([1])

seen = set()
ans = 1
while len(que):
    v = que.popleft()

    for next_v in G[v]:
        if next_v in seen: continue
        seen.add(next_v)
        que.append(next_v)
        if next_v > ans: ans = next_v

print(ans)