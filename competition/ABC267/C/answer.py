INF = 10**18

def cumulative_sum(array):
    n = len(array)
    cumsum = [0] * (n+1)
    for i in range(n):
        cumsum[i+1] = cumsum[i] + array[i]
    return cumsum

n, m = map(int, input().split())
A = list(map(int, input().split()))
S = cumulative_sum(A)

ans = sum([(i+1) * a for i, a in enumerate(A[0:m])])
prev = ans
for i in range(1, n-m+1):
    curr = prev - (S[i-1+m] - S[i-1]) + A[i+m-1] * m
    ans = max(ans, curr)
    prev = curr

print(ans)
    