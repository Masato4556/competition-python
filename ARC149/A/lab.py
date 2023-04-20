# テストデータ生成など、回答とは関係のないコードを実行するファイル

def f(n):
    ret = 1
    for i in range(n):
        ret *= 10
        ret += 1
    return ret

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


for i in range(20):
    print(f(i), prime_factorize(f(i)))
