

from functools import lru_cache


MOD = 998244353


def modadd(x, y):
    return (x+y) % MOD


def modsub(x, y):
    return (x-y) % MOD


def modmul(x, y):
    return (x*y) % MOD


def moddiv(x, y):
    return x * modpow(y, MOD-2)


@lru_cache(None)
def modpow(x, y):
    return pow(x, y, MOD)


N, X = map(int, input().split())
T = list(map(int, input().split()))

dp = [0 for _ in range(X+1)]
dp[0] = 1

ans = 0
for i in range(X+1):
    if dp[i] == 0:
        continue
    for j in range(N):
        if i+T[j] > X:
            if j == 0:
                ans = modadd(ans, moddiv(dp[i], N))
            continue
        dp[i+T[j]] = modadd(dp[i+T[j]], moddiv(dp[i], N))

print(ans)
