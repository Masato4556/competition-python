from collections import deque

def topological_sort(n, G, in_degs): # TODO: きちんと動くかチェックする
    que = deque()
    is_sorted_uniquely = True

    # 入次数が0のノードをキューに追加
    for i in range(n):
        if in_degs[i]==0:
            que.append(i)
    
    order = []
    while que:
        if len(que) > 1: is_sorted_uniquely = False
        v = que.popleft()
        order.append(v)
        for adj in G[v]:
            in_degs[adj] -= 1 
            if in_degs[adj]==0: #入次数が0になったら、キューに入れる
                que.append(adj)
     
    has_cycles = len(order) != n
    return (order, is_sorted_uniquely, has_cycles)

n, m = map(int, input().split())
G = [[] for _ in range(n)]
deg = [0 for _ in  range(n)]
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if x in G[y]: continue

    G[y].append(x)
    deg[x] += 1

for i in range(n):
    G[i].sort(reverse=True)

order, is_sorted_uniquely, has_cycles = topological_sort(n, G, deg.copy())

if is_sorted_uniquely and not has_cycles:
    print('Yes')
    c = {v:i+1 for i, v in enumerate(reversed(order))}
    print(*[c[i] for i in range(n)])
else:
    print('No')