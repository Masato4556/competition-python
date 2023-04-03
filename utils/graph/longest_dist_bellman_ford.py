def longest_path(graph, start):
    # 初期化
    dist = [float('-inf') for _ in range(len(graph))] # 各ノードまでの距離をマイナス無限大で初期化
    dist[start] = 0 # 始点自身への距離は0

    # 最長距離を計算
    for i in range(len(graph)):
        for j in range(len(graph)):
            for adj_node, weight in graph[j]: # 各ノードについて、そのノードに接続しているノードを探索
                if dist[j] != float('-inf') and dist[j] - weight > dist[adj_node]: # ノードjまでの最長距離が分かっている場合、そのノードを経由した場合の距離がより長い場合は更新
                    dist[adj_node] = dist[j] - weight
                    if i == len(graph) - 1: # 負の閉路が存在する場合、len(graph)回目のループでも更新が起きるため、それを検知して終了する
                        return None

    # 各ノードまでの距離をプラスに戻す
    for i in range(len(dist)):
        dist[i] = -dist[i]

    return dist
