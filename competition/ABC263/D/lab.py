# テストデータ生成など、回答とは関係のないコードを実行するファイル
from itertools import cycle

input_path = "./testcases/input/7.txt"
N = 2 * (10**5)
L = 0
R = 0

with open(input_path, mode='w') as f:
    s = f.write(f'{N} {L} {R}\n')
    for i in cycle(range(2)):
        s = f.write(f"{i} ")
    s = f.write("\n")

