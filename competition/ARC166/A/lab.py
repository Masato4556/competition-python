# テストデータ生成など、回答とは関係のないコードを実行するファイル

from random import choice
N = 5

chrs = ["A", "B", "C"]

X = []
Y = []
for i in range(5):
    X.append(choice(chrs))
    Y.append(choice(chrs))

print("".join(X), "".join(Y))
