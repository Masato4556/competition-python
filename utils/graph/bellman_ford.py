# O(EV)
def bellman_ford(start, graph):
    d = [float('inf')]*n # 各頂点への最小コスト
    d[start] = 0 # 自身への距離は0
    for i in range(n):
        update = False # 更新が行われたか
        for x, edges in enumerate(graph):
            for y, cost in edges:
                if d[y] > d[x] + cost:
                    d[y] = d[x] + cost
                    update = True
        if not update:
            break
        # 負閉路が存在
        if i == n - 1:
            return -1
    return d

n, w = [int(x) for x in input().split()]
g = [[] for _ in range(n)]
for _ in range(w):
    x, y, cost = [int(x) for x in input().split()] # 始点,終点,コスト
    g[x].append([y, cost])
    g[y].append([y, cost]) # 有向グラフでは削除
print(bellman_ford(0, g))

# costの値を-1倍してこの関数を実行し、結果も-1倍することで、最長路を求めることができる