def f(n, A, dp):
    result = 0
    for a in A:
        if n - a < 0: continue
        nas = (n-a) - dp[n-a] # 石の数がn-a個の時に後攻が取れる石の数
        result = max(result, a + nas)
    return result

n, k = map(int, input().split())
A = list(map(int, input().split()))

dp = [-1] * (n + 1) 
dp[0] = 0

for i in range(1, n+1):
    dp[i] = f(i, A, dp)

print(dp[-1])
