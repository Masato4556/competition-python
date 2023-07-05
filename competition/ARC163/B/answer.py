
N, M = map(int, input().split())
left, right, *A = list(map(int, input().split()))

A.sort()
len_A = len(A)

ans = 10**12
for li in range(len_A-M+1):
    ri = li+M-1
    ans = min(ans, max(0, left - A[li]) + max(0, A[ri] - right))

print(ans)
