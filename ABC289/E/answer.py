from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    C = list(map(int, input().split()))

    G = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    print(G)
