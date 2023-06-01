
N, Q = map(int, input().split())

G = [set() for _ in range(N)]

convert = dict()
uniques = set(range(N))

for i in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        v1 = query[1]-1
        v2 = query[2]-1
        G[v1].add(v2)
        G[v2].add(v1)
        if v1 in uniques:
            uniques.remove(v1)
        if v2 in uniques:
            uniques.remove(v2)

    else:
        v1 = query[1]-1
        uniques.add(v1)
        ans = 0
        remove = set()
        for j in G[v1]:
            G[j].remove(v1)
            remove.add(j)
            if len(G[j]) == 0:
                uniques.add(j)
        for r in remove:
            G[v1].remove(r)
    print(len(uniques))
