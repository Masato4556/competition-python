n, m = map(int, input().split())

G = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

for i in range(n):
    G[i].sort()
    print(len(G[i]), *[v+1 for v in G[i]])

