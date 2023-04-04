# O(√N)
def prime_factorize(n):
    ret = set()
    i = 2
    while i**2 <= n:
        e = 0
        while n % i == 0:
            n //= i
            e += 1
        if e > 0:
            ret.add(i)
        i += 1
    if n > 1: 
        ret.add(n)
    return ret


A, X, M = map(int, input().split())

print(prime_factorize(A), X, prime_factorize(M))

ans = 0
t = 1
for _ in range(X):
    ans += t % M
    ans %= M 
    t *= A

print(ans)
exit()

# if M % A