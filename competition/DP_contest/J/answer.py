# lru_cacheを用いな実装にすると,TLEを回避できた。
# lru_cacheって実は重いのか？

import sys
sys.setrecursionlimit(10**9)

N = int(input())
cnts = [0] * 4

for a in map(int, input().split()):
    cnts[a] += 1

# なるべく最低限サイズに配列にすることでACした。
dp = [[[-1] * (cnts[3]+1) for _ in range(cnts[2]+cnts[3]+1)] for _ in range(N+1)]
dp[0][0][0] = 0

# キャッシュを用いるより、dp配列内に値があれば返すような関数を自作して用いる方が早いかも
def f(a, b, c):
    if dp[a][b][c] > -1:
        return dp[a][b][c]
    ret = N
    if a > 0:
        ret += f(a-1, b, c) * a
    if b > 0:
        ret += f(a+1, b-1, c) * b
    if c > 0:
        ret += f(a, b+1, c-1) * c
    ret /= a+b+c
    dp[a][b][c] = ret
    return ret

print(f(cnts[1], cnts[2], cnts[3]))
