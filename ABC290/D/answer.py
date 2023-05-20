from math import ceil


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


T = int(input())
for _ in range(T):
    N, D, K = map(int, input().split())

    g = gcd(N, D)

    vv = N // g
    shift_cnt = ceil(K / vv) - 1

    KK = K - shift_cnt*vv
    print((shift_cnt + (KK-1) * D) % N)
