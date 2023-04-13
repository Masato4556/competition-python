# a > bの時は、X+Y = a-bとなる


from random import randint
from math import ceil
# テストデータ生成など、回答とは関係のないコードを実行するファイル

# a = 4394
# b = 993298361

a = 95392025
b = 569922442

# a = 8
# b = 16

# a = 11
# b = 23

# a = randint(1, 10**5)
# b = randint(1, 10**5)

# if a > b:
#     a, b = b, a



print(f"1 <= k <= {(b-1)/(a+1)}")
max_k = ceil((b-1)/(a+1))

ans = 10**18
for k in range(1, max_k + 1):
    x = max(ceil(b / k) - a, 0)
    y = k * (a + x) - b
    print(k, x, y, a+x, b+y, (b+y)/(a+x))
    # print(x, y, x+y, ans)
    if x+y < ans:
        ans = x+y

print(ans)
