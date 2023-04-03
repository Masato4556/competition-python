from collections import deque

# 到達可能かを調べる
def bfs(graph, start):
    # 訪問済みのノードを管理するための集合
    visited = set()
    # 訪問予定のノードを管理するためのキュー
    queue = deque([start])

    while queue:
        # キューの先頭からノードを取り出す
        node = queue.popleft()
        # 取り出したノードが訪問済みでなければ、訪問済みにする
        if node not in visited:
            visited.add(node)
            # 取り出したノードに隣接するノードをキューに追加する
            queue.extend(graph[node] - visited)

    # 訪問済みのノードを返す
    return visited

# 幅優先探索により最短経路を求める関数
def bfs_shortest_path(graph, start, end):
    # 各ノードについて、そこまでの最短経路の長さを保持するための辞書
    shortest_path = {start: [start]}
    # キューに開始ノードを追加する
    queue = deque([start])

    # キューが空になるまで探索を続ける
    while queue:
        # キューの先頭からノードを取り出す
        current = queue.popleft()
        # 目的地に到達した場合、最短経路を返す
        if current == end:
            return shortest_path[current]
        # 隣接するノードについて、まだ最短経路が決まっていなければ、最短経路を更新する
        for neighbor in graph[current]:
            if neighbor not in shortest_path:
                shortest_path[neighbor] = shortest_path[current] + [neighbor]
                queue.append(neighbor)

    # 目的地に到達できなかった場合、Noneを返す
    return None


# 二部グラフ判定
