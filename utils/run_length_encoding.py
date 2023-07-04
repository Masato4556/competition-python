# 連続する要素を(値、個数)で表すことで圧縮する手法
# ソートしてから実行すれば、

# これを用いてACできる問題 127D

# 参考
# https://output-zakki.com/run_length_encoding/


# 例　127D
# ランレングス圧縮しない場合、配列にCをB個追加するという操作の計算量がO(B)になる
# ランレングス圧縮した場合、計算量がO(1)になる
from itertools import groupby
import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))

# ランレングス圧縮
A.sort(reverse=True)
AA = [(-1 * k, len(list(g))) for k,g in groupby(A)]

for _ in range(M):
    b, c = map(int, input().split())
    heapq.heappush(AA, (-1 * c, b))

cnt = 0 
ans = 0
while cnt < N:
    v, n = heapq.heappop(AA)
    v *= -1
    if cnt + n > N:
        ans += v * (N - cnt)
        break
    else:
        ans += v * n
        cnt += n


print(ans)