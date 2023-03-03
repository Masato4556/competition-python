
def cumulative_sum(array):
    n = len(array)
    cumsum = [0] * (n+1)
    for i in range(n):
        cumsum[i+1] = cumsum[i] + array[i]
    return cumsum

def binary_search(S, start, target):
    left, right = start, len(S) - 1
    while left <= right:
        mid = (left + right) // 2
        if S[mid] - S[start] == target:
            return mid
        elif S[mid] - S[start] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

n, p, q, r = map(int, input().split())
targets = [p, q, r]
A = list(map(int, input().split()))
S = cumulative_sum(A)

dp = [set() for _ in range(4)]
dp[0].update([i for i in range(n)])

for i in range(3):
    for j in dp[i]:
        k = binary_search(S, j, targets[i])
        if k != -1:
            dp[i+1].add(k)
        
print("Yes" if len(dp[-1]) > 0 else "No")
