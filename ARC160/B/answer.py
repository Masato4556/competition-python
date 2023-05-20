from math import floor

MOD = 998244353

T = int(input())

for _ in range(T):
    N = int(input())
    ans = 0

    m = floor(N**(1/2))

    for y in range(1, m+1):
        ans += 6 * (y - 1) * (N//y - y)
        ans += 3 * (N//y - y)
        ans += 3 * (y - 1)
        ans += 1
        ans %= MOD

    print(ans)
