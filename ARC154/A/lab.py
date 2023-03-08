# テストデータ生成など、回答とは関係のないコードを実行するファイル

# n = 8
# A = 20000100 
# B = 21222322


# res = 10**18
# for i in range(2**n):
#     A_s = [s for s in str(A)]
#     B_s = [s for s in str(B)]
#     for j in range(len(A_s)):
#         if 1 << j & i:
#             A_s[j], B_s[j] = B_s[j], A_s[j]
    
#     A_ = int("".join(A_s))
#     B_ = int("".join(B_s))
#     print(A_, B_)
#     print(A_ * B_)
#     if A_ * B_ < res:
#         res = A_ * B_
#         ans = (A_ , B_)
    

# print('===')
# print(ans)
# print(res)
# print(res % 998244353 )

import time
start = time.perf_counter()
s = 0
for _ in range(10**7):
    s += 100000000000000000000
s %= 10
end = time.perf_counter()

print(round(end - start, 5))