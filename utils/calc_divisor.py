# 配列を用いる場合
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

# setを用いる場合
def calc_divisor(n):
    i = 1
    divisors = set()
    while i*i <= n:
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
        i += 1
    return divisors