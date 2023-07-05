
N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [False] * (K+1)


for i in range(1, K+1):
    for a in A:
        if i-a < 0:
            break
        if not dp[i-a]:
            dp[i] = True
            break

print("First" if dp[K] else "Second")
