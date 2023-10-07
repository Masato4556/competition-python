# 引用 https://qiita.com/wotsushi/items/c936838df992b706084c

'''
確率modや、期待値modを計算するときに利用する

modpowをキャッシュしている理由:
確率の計算にて、同じ数で割り算を行うことが多いため、
毎回mod逆元を計算せずに済むように計算結果をキャッシュする
'''
from functools import lru_cache


MOD = 10**9 + 7


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
