from collections import defaultdict

MOD = 10**9 + 7 

N, K = map(int, input().split())
A = list(map(int, input().split()))

if K == 0:
    print(1)
    exit()

dp = [[0] * (K+1) for _ in range(N+1)]
dp[0][0] += 1
dp[0][1] -= 1

for i in range(1, N+1):
    cnt = 0
    for j in range(K+1):
        cnt += dp[i-1][j]
        if cnt > 0:
            dp[i][j] += cnt
            if j+A[i-1]+1 <= K:
                dp[i][j+A[i-1]+1] -= 1

ans = 0
for c in dp[-1]:
    ans += c
    ans %= MOD
print(ans)


# 解説ではBITもしくは累積和を使えば良いと書いていた
# BITを使ったことはないので、ちゃんと勉強して理解しながら使ってみたい