import heapq

def longest_path_dijkstra(graph, start):
    # 初期化
    dist = [float('-inf') for _ in range(len(graph))] # 各ノードまでの距離をマイナス無限大で初期化
    dist[start] = 0 # 始点自身への距離は0
    prev = [None for _ in range(len(graph))] # 各ノードの親を初期化
    heap = [(0, start)] # 始点からの距離とそのノードを格納したヒープを初期化

    # 最長距離を計算
    while heap:
        d, node = heapq.heappop(heap)
        if dist[node] > d:
            continue
        for adj_node, weight in graph[node]: # 各ノードについて、そのノードに接続しているノードを探索
            if dist[node] - weight > dist[adj_node]: # ノードjまでの最長距離が分かっている場合、そのノードを経由した場合の距離がより長い場合は更新
                dist[adj_node] = dist[node] - weight
                prev[adj_node] = node
                heapq.heappush(heap, (dist[adj_node], adj_node))

    # 最長経路を復元する
    path = []
    current_node = len(graph) - 1
    while current_node is not None:
        path.append(current_node)
        current_node = prev[current_node]
    path.reverse()

    # 各ノードまでの距離をプラスに戻す
    for i in range(len(dist)):
        dist[i] = -dist[i]

    return dist, path
