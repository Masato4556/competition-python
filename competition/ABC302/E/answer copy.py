N, Q = map(int, input().split())

G = [set() for _ in range(N+Q)]

convert = dict()
max_v = N-1
removed = set()

unique_node_set = set(range(N))

for i in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        v1 = query[1]-1
        v2 = query[2]-1
        if v1 in convert:
            v1 = convert[v1]
        if v2 in convert:
            v2 = convert[v2]
        G[v1].add(v2)
        G[v2].add(v1)

        if v1 in unique_node_set:
            unique_node_set.remove(v1)
        if v2 in unique_node_set:
            unique_node_set.remove(v2)
        print(len(unique_node_set))
        continue
    else:
        v1 = query[1]-1
        max_v += 1
        convert[v1] = max_v
        removed.add(v1)
        if v1 in unique_node_set:
            unique_node_set.remove(v1)
        unique_node_set.add(max_v)

        ans = 0
        for j in G[v1]:
            if j in removed:
                continue
            flg = 0
            for v in G[j]:
                if v in removed:
                    continue
                flg = 1
                break
            if flg == 0:
                unique_node_set.add(j)
        print(len(unique_node_set))
