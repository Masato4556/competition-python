# 各エッジの重みが異なる場合は、ダイクストラ法を用いた方が良い

# 到達可能か
def dfs(graph, start):
    # 訪問済みのノードを管理するための集合
    visited = set()

    # 再帰的に探索する関数
    def dfs_recursive(node):
        # ノードが訪問済みでなければ、訪問済みにする
        if node not in visited:
            visited.add(node)
            # ノードに隣接するノードを再帰的に探索する
            for neighbor in graph[node]:
                dfs_recursive(neighbor)

    # スタートノードから再帰的に探索を開始する
    dfs_recursive(start)

    # 訪問済みのノードを返す
    return visited
