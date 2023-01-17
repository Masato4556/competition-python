# ==== 素因数分解 ====
# O(√N)
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