from collections import deque


n, m = map(int, input().split())

G = [set() for _ in range(n*2)] # i番目のロープの赤の端を2(i-1), 青の端を2(i - 1) + 1とする
for i in range(1, n+1):
    G[2 * i - 2].add(2 * i - 1)
    G[2 * i - 1].add(2 * i - 2)

for _ in range(m):
    a, b, c, d = input().split()
    a = int(a)
    c = int(c)
    i = 2 * a - 2 if b == "R" else 2 * a - 1
    j = 2 * c - 2 if d == "R" else 2 * c - 1
    G[i].add(j)
    G[j].add(i)

x = 0

cnt = 0
seen = [False ] * (n*2)
while False in seen:
    cnt += 1
    root = seen.index(False)
    que = deque([root])
    edge_num = 0
    while len(que):
        v = que.popleft()
        seen[v] = True
        for next_v in G[v]:
            if seen[next_v]: continue
            seen[next_v] = True
            edge_num += 1
            que.append(next_v)
            break
    if root in G[v] and edge_num > 1:
        x += 1

print(x, cnt - x)


