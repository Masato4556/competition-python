# 参考: G問題 https://kyopro-friends.hatenablog.com/entry/2019/01/12/231000#:~:text=%E3%81%AF%E3%81%93%E3%82%93%E3%81%AA%E6%84%9F%E3%81%98%EF%BC%81-,G%E5%95%8F%E9%A1%8C%20Longest%20Path,-%E6%9C%89%E5%90%91%E9%96%89%E8%B7%AF


from functools import lru_cache

N, M = map(int, input().split())
G = [set() for _ in range(N)]
for _ in range(M):
    x, y = map(lambda x: int(x)-1, input().split())
    G[x].add(y)

'''
longest_dist(v)は、vからスタートする最長のパスの長さを返す関数
- 再起メモ化を用いて高速化
- DAG（有効非循環グラフ）でしか使えない？

ロジック
- 出次数が0のノード(葉)の場合、0を返す
- 出次数が0でないノード(枝)の場合、エッジの移動先next_vとした時のf(next_v)の最も大きい値に1を足して返す。

グラフ内のすべてのノードで、longest_distを実行して比較することで、再長距離を求めることができる。
その場合、計算量はO(N+M)
'''
@lru_cache(None)
def longest_dist(v):
    dist = 0
    for next_v in G[v]:
        dist = max(dist, longest_dist(next_v) + 1)
    return dist

ans = 0
for i in range(N):
    ans = max(ans, longest_dist(i))
print(ans)