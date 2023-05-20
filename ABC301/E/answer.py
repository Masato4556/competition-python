from collections import deque


def popcount(x):
    x = x - ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 0x0000007f


INF = 10**18
H, W, T = map(int, input().split())

A = []
okashis = []
for h in range(H):
    A.append(input())

    for w in range(W):
        if A[h][w] == "S":
            start = (w, h)
        elif A[h][w] == "G":
            goal = (w, h)
        elif A[h][w] == "o":
            okashis.append((w, h))


okashi_cnt = len(okashis)


def f(r):
    que = deque([r])
    dist = [[-1 for _ in range(W)] for _ in range(H)]
    dist[r[1]][r[0]] = 0
    while que:
        x, y = que.popleft()

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if not (0 <= x + dx < W) or not (0 <= y + dy < H):
                continue
            if A[y+dy][x+dx] == "#":
                continue
            if dist[y+dy][x+dx] > -1:
                continue
            dist[y+dy][x+dx] = dist[y][x] + 1
            if dist[y+dy][x+dx] < T:
                que.append((x+dx, y+dy))
    return dist


s_to_o = [INF] * okashi_cnt
g_to_o = [INF] * okashi_cnt

dist = f(start)
for i in range(okashi_cnt):
    x, y = okashis[i]
    if dist[y][x] == -1:
        continue
    s_to_o[i] = dist[y][x]

dist = f(goal)
for i in range(okashi_cnt):
    x, y = okashis[i]
    if dist[y][x] == -1:
        continue
    g_to_o[i] = dist[y][x]

o_to_o = [[-1] * okashi_cnt for _ in range(okashi_cnt)]
for i in range(okashi_cnt):
    dist = f(okashis[i])
    for j in range(okashi_cnt):
        x, y = okashis[j]
        o_to_o[i][j] = dist[y][x]

dp = [[INF] * okashi_cnt for _ in range(2**okashi_cnt)]
for i in range(okashi_cnt):
    dp[1 << i][i] = s_to_o[i]

for s in range(1, 1 << okashi_cnt):
    for v in range(okashi_cnt):  # 配られる側
        if s >> v & 1:
            continue  # これから新しく訪れるノードがすでに訪れていることになっているならスキップ
        for u in range(okashi_cnt):
            if not s >> u & 1:
                continue
            new_s = s | (1 << v)
            dp[new_s][v] = min(
                dp[new_s][v], dp[s][u] + o_to_o[u][v])

ans = -1
for s in range(1 << okashi_cnt):
    for v in range(okashi_cnt):
        if dp[s][v] + g_to_o[v] <= T:
            ans = max(ans, popcount(s))
print(ans)
