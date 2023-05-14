# テストデータ生成など、回答とは関係のないコードを実行するファイル


# a = [1, 2, 3, 4, 5]
# a = [9, 2, 1, 3, 8, 7, 10, 4, 5, 6]
# n = len(a)


# def f(l, r, a):
#     ret = []
#     for i in range(len(a)):
#         if l <= i <= r:
#             ret.append(a[r+l-i])
#         else:
#             ret.append(a[i])
#     return ret


# ans = []
# for i in range(n):
#     for j in range(i, n):
#         ans.append(f(i, j, a))
# ans.sort()

# for ans_i in ans:
#     print(ans_i)

for i in range(1, 7000+1):
    print(i, end=" ")
