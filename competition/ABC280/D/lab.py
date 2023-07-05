# テストデータ生成など、回答とは関係のないコードを実行するファイル
from math import log, floor
def prime_factorize(n):
    ret = []
    i = 2
    while i**2 <= n:
        e = 0
        while n % i == 0:
            n //= i
            e += 1
        if e > 0:
            ret.append((i, e))
        i += 1
    if n > 1: 
        ret.append((n, 1))
    return ret

def f(K):
    a = 1
    for i in range(2, K+1):
        a *= i
        if a % K == 0:
            return i

def g(p, i):
    multi = 0
    while i > 0:
        i -= 1
        multi += 1
        m = multi
        while m % p == 0:
            i -= 1
            m //= p
    return multi * p

def f2(K):
    ans = 1
    for p, i in prime_factorize(K):
        ans = max(ans, g(p, i))
    return ans



for i in range(2, 10000):
    if f(i) != f2(i):
        print(i, f(i), f2(i), prime_factorize(i))


# print(g(2, 11))
# print(g(2, 12))
