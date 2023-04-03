
'''

# args
G: 隣接リストを表す辞書型データ構造
in_degs: 入次数のリスト 

# return
order: 並び替えたノードのリスト
is_sorted_uniquely: 一意にソートできるか
has_cycles: サイクルを含んでいるか

# 計算量
計算量 O(|V|+|E|) V:ノード数, E:エッジ数

# 解説

## 一意にソートできるかの確認
queに格納されているノードが２つ以上になることがあれば、queにノードを格納する順番によって結果が変わるため、一意にソートできないと言える

## 閉路の存在確認
len(order) != len(G)なら閉路あり

有向非巡回グラフの最長経路を求める際に有効
トポロジカルソートで求めた順序に従って、動的計画法で最長距離の更新を行う。
参考 https://qiita.com/keisuke-ota/items/7190e84019a8c70a9fa6#%E5%95%8F%E9%A1%8C%E6%A6%82%E8%A6%81

'''

from collections import deque

def topological_sort(G, in_degs):
    que = deque()
    is_sorted_uniquely = True
    n = len(G)

    # 入次数が0のノードをキューに追加
    for i in range(n):
        if in_degs[i]==0:
            que.append(i)

    order = []
    while que:
        if len(que) > 1: is_sorted_uniquely = False
        v = que.popleft()
        order.append(v)
        for adj in G[v]:
            in_degs[adj] -= 1
            if in_degs[adj]==0: # 入次数が0になったら、キューに入れる
                que.append(adj)

    has_cycles = len(order) != n # サイクルが存在する場合、
    return (order, is_sorted_uniquely, has_cycles)


G = [[2, 3], [0, 3], [], [2]]
in_degs = [1, 0, 2, 2]
order, is_sorted_uniquely, has_cycles = topological_sort(G, in_degs)
print("order: {}\nis_sorted_uniquely:{}\nhas_cycles:{}".format(order, is_sorted_uniquely, has_cycles))
