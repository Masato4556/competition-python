from collections import deque


n, m = map(int, input().split())

G = [set() for _ in range(n)] # i番目のロープの赤の端を2(i-1), 青の端を2(i - 1) + 1とする
degs = [0 for _ in range(n)]

for _ in range(m):
    a, b, c, d = input().split()
    a = int(a) - 1
    c = int(c) - 1
    G[a].add(c)
    G[c].add(a)
    degs[a] += 1
    degs[c] += 1
    

seen = [False] * n
ans = 0
g_cnt = 0
for i in range(n):
    if seen[i]: continue
    g_cnt += 1
    que = deque([i])

    flg = True
    while len(que):
        v = que.popleft()
        if degs[v] != 2: flg = False 
        seen[v] = True
        for next_v in G[v]:
            if seen[next_v]: continue
            que.append(next_v)

    if flg: ans += 1 


print(ans, g_cnt - ans)