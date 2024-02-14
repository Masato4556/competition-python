# テストデータ生成など、回答とは関係のないコードを実行するファイル

from math import floor, ceil


for i in range(10**17 + 1):
    if (i // 2, (i+1)//2) != (floor(i/2), ceil(i/2)):
        print(i)
        exit()
