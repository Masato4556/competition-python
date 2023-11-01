from bisect import bisect_right


def cumulative_sum(arr):
    cumsum = [0]
    for v in arr:
        cumsum.append(cumsum[-1] + v)
    return cumsum


N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cumsum_A = cumulative_sum(A)
cumsum_B = cumulative_sum(B)

ans = 0

for i, csa in enumerate(cumsum_A):
    t = cumsum_A[i]
    if csa > K:
        break
    j = bisect_right(cumsum_B, K-csa)
    ans = max(ans, i+j-1)

print(ans)
