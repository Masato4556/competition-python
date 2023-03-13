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

def longest_path(graph, start):
    # 初期化
    dist = [float('-inf') for _ in range(len(graph))] # 各ノードまでの距離をマイナス無限大で初期化
    dist[start] = 0 # 始点自身への距離は0
    heap = [(-0, start)] # 優先度付きキューに始点を追加

    # 最長距離を計算
    while heap:
        d, node = heapq.heappop(heap) # 優先度付きキューから距離が最大のノードを取り出す
        if dist[node] > -d: # 取り出したノードの距離が、既に知っている最長距離よりも小さい場合はスキップ
            continue
        for adj_node, weight in graph[node]: # 取り出したノードに接続しているノードを探索
            new_d = dist[node] - weight # 取り出したノードを経由した場合の距離を計算
            if new_d > dist[adj_node]: # 計算した距離が、既に知っている最長距離よりも大きい場合は更新
                dist[adj_node] = new_d
                heapq.heappush(heap, (-new_d, adj_node)) # 更新したノードを優先度付きキューに追加

    # 各ノードまでの距離をプラスに戻す
    for i in range(len(dist)):
        dist[i] = -dist[i]

    return dist

print()
