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

n = int(input())
s = [0] * n

for i in range(1, n):
    s[i] = len(calc_divisor(i))

ans = 0
for i in range(1, n):
    ans += s[i] * s[n-i]
print(ans)

