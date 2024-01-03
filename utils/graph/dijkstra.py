import heapq


def dijkstra(adj_list, start):
    """
    adj_list: 隣接リストを表す辞書型データ構造 {u: [(v, cost), ... ], ... }
    start: 始点の頂点番号
    """
    n = len(adj_list)  # 頂点数
    dist = [float('inf')] * n  # 頂点iまでの最短距離を表すリスト
    dist[start] = 0  # 始点までの距離は0
    heap = [(0, start)]  # ヒープ（優先度付きキュー）を用いる
    heapq.heapify(heap)

    while heap:
        d, u = heapq.heappop(heap)  # ヒープから最小の距離を持つ頂点を取り出す
        if d > dist[u]:  # 取り出した頂点の距離が現在の最短距離よりも大きい場合はスキップする
            continue
        for v, cost in adj_list[u]:  # 頂点uに隣接する各頂点vについて
            if dist[v] > dist[u] + cost:  # 頂点vまでの距離が現在の最短距離よりも小さい場合は更新する
                dist[v] = dist[u] + cost
                heapq.heappush(heap, (dist[v], v))

    return dist

# costの値を-1倍してこの関数を実行し、結果も-1倍することで、最長路を求めることができる


def dijkstra_path(adj_list, start): # 動作確認できてない
    """
    adj_list: 隣接リストを表す辞書型データ構造 {u: [(v, cost), ... ], ... }
    start: 始点の頂点番号
    """
    n = len(adj_list)  # 頂点数
    dist = [float('inf')] * n  # 頂点iまでの最短距離を表すリスト
    dist[start] = 0  # 始点までの距離は0
    prev = [-1] * n
    heap = [(0, start)]  # ヒープ（優先度付きキュー）を用いる
    heapq.heapify(heap)

    while heap:
        d, u = heapq.heappop(heap)  # ヒープから最小の距離を持つ頂点を取り出す
        if d > dist[u]:  # 取り出した頂点の距離が現在の最短距離よりも大きい場合はスキップする
            continue
        for v, cost in adj_list[u]:  # 頂点uに隣接する各頂点vについて
            if dist[v] > dist[u] + cost:  # 頂点vまでの距離が現在の最短距離よりも小さい場合は更新する
                dist[v] = dist[u] + cost
                heapq.heappush(heap, (dist[v], v))
                prev[v] = u

    return (dist, prev)


def gen_path_from_prev(prev, end):
    v = end
    path = []
    while True:
        path.append(v)
        v = prev[v]
        if v == -1:
            break
    return path


# https://judge.yosupo.jp/problem/shortest_path
testcase = [
    (5, 7, 2, 3),
    [
        (0, 3, 5),
        (0, 4, 3),
        (2, 4, 2),
        (4, 3, 10),
        (4, 0, 7),
        (2, 1, 5),
        (1, 0, 1),
    ]
]

N, M, s, t = testcase[0]

G = [set() for _ in range(N)]
for a, b, c in testcase[1]:
    G[a].add((b, c))

dist, prev = dijkstra_path(G, s)

v = t
path = gen_path_from_prev(prev, t)

print(dist[t], len(path) - 1)

path.reverse()

for i in range(len(path) - 1):
    print(path[i], path[i+1])