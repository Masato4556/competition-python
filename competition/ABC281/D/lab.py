# テストデータ生成など、回答とは関係のないコードを実行するファイル
from itertools import combinations_with_replacement


N = 100
K = 100
D = 5

arr = list(range(N))

dp = [[] for _ in range(D)]


for i in combinations_with_replacement(arr, K):
    if sum(i) % D != 0: continue
    print(i)