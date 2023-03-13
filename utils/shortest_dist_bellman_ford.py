'''
ベルマンフォード法
ある頂点から他の頂点への最短距離を求めるアルゴリズム。
ダイクストラ法より低速だが、負のコストを持つ辺があっても利用可能。
'''

class Edge {
    def __init__(this, start, end, weight):
        this.start = start
        this.end = end
        this.weight = weight
}

# O(EV)
def bellman_ford(start, n, edges):
    d = [float('inf')] * n # 各頂点への最小コスト
    d[start] = 0 # 自身への距離は0
    for i in range(n):
        update = False # 更新が行われたか
        for x, y, z in g:
            if d[y] > d[x] + z:
                d[y] = d[x] + z
                update = True

        if not update: # 最小コストが更新されなかったら終了
            break

        if i == n - 1: # 負閉路が存在
            return -1
    return d

n, m = [int(x) for x in input().split()] # n:頂点数, m:辺の数

edges = []
for _ in range(m):
    x, y, z = [int(x) for x in input().split()] # 始点,終点,コスト
    edges.append(Edge(x, y, z))
    edges.append(Edge(y, x, z)) # 有向グラフでは削除

print(bellman_ford(0, n, edges))

# 経路復元したい場合、親ノードを格納する配列を用意する