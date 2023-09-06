
def popcount(x):
    x = x - ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 0x0000007f


N, M = map(int, input().split())

# エッジの管理
NOTHING = -1  # エッジが存在しない場合の値
G = [[NOTHING for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1

    # G[エッジの始点][エッジの終点] = 距離
    G[a][b] = c
    G[b][a] = c

dp = [[0] * N for _ in range(2**N)]

for S in range(2**N):
    if popcount(S) == 0:  # 任意のノードからスタートできるので、S={}の状態は存在しない
        continue
    for next_v in range(N):  # 次に進むノード
        for v in range(N):  # 現在のノード
            if G[v][next_v] == NOTHING:  # 経路がない
                continue
            if not (S >> v) & 1 and S != 0:  # すでに訪れたノードの集合(S)に、現在いるノード(v)が含まれていない
                continue

            if (S >> next_v) & 1 == 0:
                if dp[S][v] + G[v][next_v] > dp[S | (1 << next_v)][next_v]:
                    dp[S | (1 << next_v)][next_v] = dp[S][v] + G[v][next_v]

# 今回の問題は全てのノードを通り切る必要はないため、
# dp内の最大値が答えになる
print(max([max(v) for v in dp]))
