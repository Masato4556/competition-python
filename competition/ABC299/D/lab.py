# テストデータ生成など、回答とは関係のないコードを実行するファイル


from random import randint



N = 10

S = [randint(0, 1) for _ in range(N)]
S[0] = 0

print(S)

left = 1
right = N
while True:
    mid = (left + right) // 2


    print(f"? {mid}")
    # s_i = int(input())
    print("ret {S[mid-1]}")
    s_i = S[mid-1]
    if s_i == 0:
        left = mid
    else:
        right = mid

    if right - left == 1:
        print(f"! {left}")
        exit()
