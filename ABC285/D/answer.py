def dfs(v, G, seen, finished):
    ret = True
    seen[v] = True
    for v2 in G[v]:
        if seen[v2]:
            if not finished[v2]: return False
            continue
        ret &= dfs(v2, G, seen, finished)
    finished[v] = True
    return ret

n = int(input())

G = [[] for _ in range(2 * n)]
name2index = dict()

for _ in range(n):
    s, t = input().split()
    u = name2index.setdefault(s, len(name2index))
    v = name2index.setdefault(t, len(name2index))
    G[u].append(v)

name_num = len(name2index)
seen = [False for _ in range(name_num)]
finished = [False for _ in range(name_num)]

ans = "Yes"
for v in range(name_num):
    if seen[v]: continue
    if not dfs(v, G, seen, finished): ans = "No"

print(ans)