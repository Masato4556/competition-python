
class Edge:
    def __init__(self, to, dist):
        self.to = to
        self.dist = dist


NOTHING = -1

N, M = map(int, input().split())

G = [[-1 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    G[a][b] = c
    G[b][a] = c

dp = [[0] * N for _ in range(2**N)]


for S in range(2**N):
    for v in range(N):
        for u in range(N):
            if G[u][v] == NOTHING:
                continue
            if not (S >> u) & 1 and S != 0:
                continue
            if (S >> u) & 1:
                if dp[S][u] + G[u][v] > dp[S | (1 << v)][v]:
                    dp[S | (1 << v)][v] = dp[S][u] + G[u][v]
            print(bin(S), v, u, dp[S | (1 << v)][v], dp[S][u],  G[u][v])

for A in dp:
    print(max(A))

path = []
    # for a in A:
