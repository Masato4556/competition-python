from functools import lru_cache

MOD = 998244353


def moddiv(x, y):
    return (x * modpow(y, MOD-2)) % MOD


@lru_cache(None)
def modpow(x, y):
    return pow(x, y, MOD)


def solve():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    div = N
    for a in A:
        ans += moddiv(a, div)
        ans %= MOD
        div = moddiv(div, (1 + moddiv(1, N)))

    return ans


print(solve())