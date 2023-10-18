
from math import ceil, factorial

MOD = 10**9 + 7

def modinv(a, mod=MOD):
    return pow(a, mod-2, mod)

def permutation(n, r, mod=MOD):
    if n < r:
        return 0
    factorial(n) * modinv(factorial(n - r))

def combination(n, r, mod=MOD):
    if n < r:
        return 0
    return factorial(n) * modinv(factorial(r)) * modinv(factorial(n - r)) % mod

def nhr(n, r):
    return combination(n+r-1, r-1)

S = int(input())

ans = 0
for i in range(1, ceil(S//3)+1):
    ans += int(nhr(S - 3 * i, i))
    ans %= MOD

print(ans)