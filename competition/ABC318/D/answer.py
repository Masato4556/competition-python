from collections import defaultdict

def popcount(x):
    x = x - ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 0x0000007f


N = int(input())

G = [[0 for _ in range(N)] for _ in range(N)] 


for v in range(N-1):
    for i, cost in enumerate(map(int, input().split())):
        G[v][v+1+i] = cost
        G[v+1+i][v] = cost

dp = [0 for _ in range(2**N)]

for s in range(2**N):
    cnt = popcount(s)
    if cnt == 0 or cnt == 1:
        dp[s] = 0
    elif cnt == 2:
        selected = []
        for i in range(N):
            if s & (1 << i):
                selected.append(i)
        dp[s] = G[selected[0]][selected[1]]

    for v in range(N):
        if s & (1 << v):
            continue
        for u in range(N):
            if v == u:
                continue
            if s & (1 << u):
                continue
            dp[s|(1<<v | 1<<u)] = max(dp[s|(1<<v | 1<<u)], dp[s] + G[v][u])
            

print(dp[-1])

            