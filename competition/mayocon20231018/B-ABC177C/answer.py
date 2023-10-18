
def cumulative_sum(array):
    n = len(array)
    cumsum = [0] * (n+1)
    for i in range(n):
        cumsum[i+1] = cumsum[i] + array[i]
    return cumsum

N = int(input())
A = list(map(int, input().split()))

MOD = 10**9+7

cumsum = cumulative_sum(A)

ans = 0
for i in range(N):
    ans += A[i] * cumsum[i]
    ans %= MOD

print(ans)
