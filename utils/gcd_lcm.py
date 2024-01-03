# 最大公約数 𝑂(logmin(𝑎,𝑏))
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# 最小公倍数 𝑂(logmin(𝑎,𝑏))
def lcm(a, b):
    g = gcd(a, b)
    return a // g * b  # a * b // g と書くよりもオーバーフローになりにくい
