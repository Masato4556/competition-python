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
