from itertools import combinations
n, m = map(int, input().split())

G = [set() for _ in range(n)]

for i in range(m):
    X = list(map(int, input().split()))[1:]
    for c in combinations(X, 2):
        G[c[0]-1].add(c[1]-1)
        G[c[1]-1].add(c[0]-1)

print("Yes" if all([len(g) == n-1 for g in G]) else "No")
