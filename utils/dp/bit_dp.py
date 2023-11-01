# 全ての地点を経由するための最短距離を求める問題のテンプレート
# N: 地点の数
# M: エッジの数
# v,u,c: v~u間のエッジを渡るコストc

# 下記のコードがちゃんと動くかまだ確認していない

INF = float('inf')

N, M = map(int, input().split())
G = [[INF for _ in range(N)] for _ in range(N)]  # エッジがない区間はINFを代入
for _ in range(M):
    v, u, c = map(int, input().split())
    G[v-1][u-1] = c
    G[u-1][v-1] = c

dp = [[INF for _ in range(N)] for _ in range(2**N)]
dp[0][0] = 0

for s in range(2**N):
    for nv in range(N):
        for v in range(N):
            if not (s >> v) & 1 and s != 0:
                continue
            if not (s >> nv) & 1:  # 配られる側の要素が集合に含まれていない
                cost = dp[s][v] + G[v][nv]
                if cost < dp[s | (1 << nv)][nv]:
                    dp[s | (1 << nv)][nv] = cost

ans = min([dp[2**N-1][i] for i in range(N)])
print(ans if ans != INF else -1)
