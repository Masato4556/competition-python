from collections import deque, defaultdict
import heapq
from functools import lru_cache
import sys
sys.setrecursionlimit(10 ** 9)

mod = 998244353

N, A, B, P, Q = map(int, input().split())

# 先攻がAマス、後攻がBマスにいて、直前にT(0なら先攻)がダイスを振ったという状況になる確率dp[A][B][T]
dp = [[[-1] * 2 for _ in range(N+1)] for _ in range(N+1)]

dp[0][0][1] = 1

def f(a, b, t):
    if dp[a][b][t] != -1:
        return dp[a][b][t]

    ret = 0

    if t == 0: # 直前にサイコロを振ったのが先
        for i in range(1, P+1):
            if a-i < 0: 
                continue
            if a == N:
                ret += f(a-i, b, 1) * pow(P, mod-2, mod) * (P+1-i)
                # ret += f(a-i, b, 1) / P * (P+1-i)
            else:
                ret += f(a-i, b, 1) * pow(P, mod-2, mod)
                # ret += f(a-i, b, 1) / P
            ret %= mod
    else:
        for i in range(1, Q+1):
            if b-i < 0: 
                continue
            if b == N:
                ret += f(a, b-i, 0) * pow(Q, mod-2, mod) * (Q+1-i)
                # ret += f(a, b-i, 0) / Q * (Q+1-i)
            else:
                ret += f(a, b-i, 0) * pow(Q, mod-2, mod)
                # ret += f(a, b-i, 0) / Q
            ret %= mod
    
    dp[a][b][t] = ret
    return ret

ans = 0
for i in range(N-1, -1, -1):
    a = f(N, i, 0)
    if a != -1:
        ans += a
        ans %= mod
print(ans)


# 何が間違っているかわからない
# 一度解説の方法で解いてみる