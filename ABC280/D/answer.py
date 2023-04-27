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


K = int(input())

ans = 1
for p, i in prime_factorize(K):
    ans = max(ans, g(p, i))

print(ans)