N, M = map(int, input().split())
S = [input() for _ in range(N)]
G = [set() for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        cnt = 0
        for k in range(M):
            if S[i][k] != S[j][k]:
                cnt += 1
        if cnt == 1:
            G[i].add(j)
            G[j].add(i)

dp = [[0 for _ in range(N)] for _ in range(2**N)]

for i in range(N):
    dp[1 << i][i] = 1

for s in range(2**N):
    for v in range(N):
        if s >> v & 1:
            continue
        for u in range(N):
            if not (s >> u & 1):
                continue
            if dp[s][u] and v in G[u]:
                dp[s | 1 << v][v] = 1

for i in range(N):
    if dp[2**N-1][i] == 1:
        print("Yes")
        exit()
print("No")
