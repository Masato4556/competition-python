from math import floor

def eratosthenes(n):
    is_prime = [True] * (n+1)
    is_prime[0], is_prime[1] = False, False

    i = 1
    while i^2 < n-1:
        i += 1

        if not is_prime[i]:
            continue

        j = i * 2
        while j <= n:
            is_prime[j] = False
            j += i

    return [i for i, p in enumerate(is_prime) if p == True]

N = int(input())

primes = eratosthenes(floor(pow(N // 12, 0.5)))
max_a = floor(pow(N, 0.2))
p_len = len(primes)
ans = 0
for i in range(p_len):
    if primes[i] > max_a: break
    a_2 = primes[i] ** 2
    b_max = floor(pow(N // a_2, 1/3))
    for j in range(i+1, p_len):
        b = primes[j]
        if b >= b_max: break
        c_max = floor(pow(N // a_2 // b, 1/2))
        for k in range(j+1, p_len):
            c_2 = primes[k] ** 2
            if a_2 * b * c_2 > N: break
            ans += 1


print(ans)
