from bisect import bisect_left


def cumulative_sum(array):
    n = len(array)
    cumsum = [0] * (n+1)
    for i in range(n):
        cumsum[i+1] = cumsum[i] + array[i]
    return cumsum


N, M, P = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


A.sort()
B.sort()

cs_b = cumulative_sum(B)

ans = 0
for a in A:
    max_b = P-a
    pi = bisect_left(B, max_b)
    ans += a * pi + cs_b[pi]
    ans += (M-pi) * P
print(ans)
