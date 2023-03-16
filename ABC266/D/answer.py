N = int(input())

dp = [[-1] * 5 for _ in range(N+1)]
dp[0][0] = 0
for _ in range(N):
    T, X, A = map(int, input().split())
    for i in range(5):
        

print(dp)
