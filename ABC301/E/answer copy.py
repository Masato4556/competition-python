from collections import deque


def popcount(x):
    '''xの立っているビット数をカウントする関数
    (xは64bit整数)'''

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f  # 8bitごと
    x = x + (x >> 8)  # 16bitごと
    x = x + (x >> 16)  # 32bitごと
    x = x + (x >> 32)  # 64bitごと = 全部の合計
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
poses = [start] + okashis + [goal]
N = okashi_cnt + 2
G = [dict() for _ in range(N)]

for i in range(N):
    p = poses[i]
    que = deque([p])
    dist = [[-1 for _ in range(W)] for _ in range(H)]
    dist[p[1]][p[0]] = 0
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

    for j in range(N):
        x, y = poses[j]
        if i == j:
            continue
        if dist[y][x] == -1:
            continue
        G[i][j] = dist[y][x]
        G[j][i] = dist[y][x]

dp = [[INF] * N for _ in range(2**N)]
dp[1][0] = 0

for s in range(1 << N):
    for v in range(N):  # 　配られる側
        for u in range(N):  # 配る側
            if not s >> u & 1 and s != 0:
                continue
            if s >> v & 1 == 0:
                if v not in G[u]:
                    continue
                dp[s | (1 << v)][v] = min(
                    dp[s | (1 << v)][v], dp[s][u] + G[u][v])


ans = -1
for i in range(2**okashi_cnt):
    t = 1
    t |= 1 << (N-1)
    t |= i << 1
    if dp[t][-1] <= T:
        ans = max(ans, popcount(i))

print(ans)
