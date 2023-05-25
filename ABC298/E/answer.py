from collections import deque, defaultdict
import heapq
from functools import lru_cache
import sys
sys.setrecursionlimit(10 ** 9)

MOD = 998244353

class ModInt:
    def __init__(self, x):
        self.x = x % MOD

    def __str__(self):
        return str(self.x)

    __repr__ = __str__

    def __add__(self, other):
        return (
            ModInt(self.x + other.x) if isinstance(other, ModInt) else
            ModInt(self.x + other)
        )

    def __sub__(self, other):
        return (
            ModInt(self.x - other.x) if isinstance(other, ModInt) else
            ModInt(self.x - other)
        )

    def __mul__(self, other):
        return (
            ModInt(self.x * other.x) if isinstance(other, ModInt) else
            ModInt(self.x * other)
        )

    def __truediv__(self, other):
        return (
            ModInt(
                self.x * pow(other.x, MOD - 2, MOD)
            ) if isinstance(other, ModInt) else
            ModInt(self.x * pow(other, MOD - 2, MOD))
        )

    def __pow__(self, other):
        return (
            ModInt(pow(self.x, other.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(self.x, other, MOD))
        )

    __radd__ = __add__

    def __rsub__(self, other):
        return (
            ModInt(other.x - self.x) if isinstance(other, ModInt) else
            ModInt(other - self.x)
        )

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return (
            ModInt(
                other.x * pow(self.x, MOD - 2, MOD)
            ) if isinstance(other, ModInt) else
            ModInt(other * pow(self.x, MOD - 2, MOD))
        )

    def __rpow__(self, other):
        return (
            ModInt(pow(other.x, self.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(other, self.x, MOD))
        )


N, A, B, P, Q = map(int, input().split())

# 先攻がAマス、後攻がBマスにいて、直前にT(0なら先攻)がダイスを振ったという状況になる確率dp[A][B][T]
dp = [[[-1] * 2 for _ in range(N+1)] for _ in range(N+1)]

dp[0][0][1] = ModInt(1)

def f(a, b, t):
    if dp[a][b][t] != -1:
        return dp[a][b][t]

    ret = ModInt(0)

    if t == 0: # 直前にサイコロを振ったのが先
        for i in range(1, P+1):
            if a-i < 0: 
                continue
            if a == N:
                ret += f(a-i, b, 1) / P * (P+1-i)
                # ret += f(a-i, b, 1) / P * (P+1-i)
            else:
                ret += f(a-i, b, 1) / P
                # ret += f(a-i, b, 1) / P
    else:
        for i in range(1, Q+1):
            if b-i < 0: 
                continue
            if b == N:
                ret += f(a, b-i, 0) / Q * (Q+1-i)
                # ret += f(a, b-i, 0) / Q * (Q+1-i)
            else:
                ret += f(a, b-i, 0) / Q
                # ret += f(a, b-i, 0) / Q
    
    dp[a][b][t] = ret
    return ret

ans = ModInt(0)
for i in range(N):
    a = f(N, i, 0)
    ans += a
print(ans)


# 何が間違っているかわからない
# 一度解説の方法で解いてみる