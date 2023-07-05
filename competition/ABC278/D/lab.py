# テストデータ生成など、回答とは関係のないコードを実行するファイル
import time


for n in (1, 10, 100, 1000, 10000, 100000):

    result = 0
    for _ in range(100):
        start = time.perf_counter()


        A = [0] * n
        A[-1] = 1

        end = time.perf_counter()
        run_time = end - start
        result += run_time
        # print("実行時間: {}秒".format(run_time))

    print(n)
    print(result / 100)