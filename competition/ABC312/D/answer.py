
MOD = 998244353
S = input()

len_s = len(S)

dp = [[0 for _ in range(len_s // 2 + 1)] for _ in range(len_s + 1)]
dp[0][0] = 1

if S[0] == ")":
    print(0)
    exit()

for i in range(len_s):
    for v in range(len_s//2+1):
        if S[i] != ")" and v < len_s//2:
            dp[i+1][v+1] += dp[i][v]
            dp[i+1][v+1] %= MOD
        if S[i] != "(" and v > 0:
            dp[i+1][v-1] += dp[i][v]
            dp[i+1][v-1] %= MOD

print(dp[-1][0] % MOD)
