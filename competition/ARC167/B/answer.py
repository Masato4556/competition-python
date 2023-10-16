from math import log
A, B = map(int, input().split())


def calc_divisor(n):
    i = 1
    divisors = []
    while i*i <= n:
        if n % i == 0:
            divisors.append(i)
            q = n // i
            if q != i:
                divisors.append(q)
        i += 1

    divisors.sort()
    return divisors


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


divisors = calc_divisor(A**B)
# primes = prime_factorize(A**B)
# p_num = len(primes)

# counts = [0] * len(primes)
# for divisor in divisors:
#     for i in range(p_num):
#         if divisor % primes[i] == 0:
#             counts[i] += 1
# print(counts)
