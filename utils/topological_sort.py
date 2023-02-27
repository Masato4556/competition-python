
from collections import deque

# n: ノード
# G: Graph
# in_degs: 入次数のリスト 
# 計算量 O(|V|+|E|) V:ノード数, E:エッジ数
def topological_sort(n, G, in_degs): # TODO: きちんと動くかチェックする
    que = deque()

    # 入次数が0のノードをキューに追加
    for i in range(n):
        if in_degs[i]==0:
            que.append(i)
    
    order = []
    while que:
        v = que.popleft()
        order.append(v)
        for adj in G[v]:
            in_degs[adj] -= 1 
            if in_degs[adj]==0: #入次数が0になったら、キューに入れる
                que.append(adj)
     
    return order

# 閉路の存在確認
# len(order) != len(G)なら閉路あり

# 有向非巡回グラフの最長経路を求める際に有効
# トポロジカルソートで求めた順序に従って、動的計画法で最長距離の更新を行う。
# 参考 https://qiita.com/keisuke-ota/items/7190e84019a8c70a9fa6#%E5%95%8F%E9%A1%8C%E6%A6%82%E8%A6%81