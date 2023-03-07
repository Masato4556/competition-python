def prime_factorize(n):
    ret = []
    i = 2
    while i**2 <= n:
        e = 0
        while n % i == 0:
            n //= i
            e += 1
        if e > 0:
            ret.append(i)
        i += 1
    if n > 1:
        ret.append(n)
    return ret

n = int(input())

for i in range(1, n+1):
    p = prime_factorize(i)
    s = set([1])
    for i in  range(2**len(p)):
        t = 1
        for j in range(len(p)):
            if 1 << j & i:
                t *= p[j]
        s.add(t)
    print(s)
    print(p)
    

