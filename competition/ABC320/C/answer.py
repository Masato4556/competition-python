
M = int(input())
S = [list(map(int, input())) for _ in range(3)]

dp = [[[False] * 8 for _ in range(3*M)] for _ in range(10)]
for i in range(10):
    dp[i][0][0] = True
    for j in range(3):
        if S[j][0] == i:
            dp[i][0][1 << j] = True

for t in range(1, M * 3):
    for i in range(10):
        for k in range(8):
            dp[i][t][k] = dp[i][t-1][k]

    for j in range(3):
        for k in range(8):
            if dp[S[j][t % M]][t-1][k]:
                dp[S[j][t % M]][t][k|(1<<j)] = True
                
    for i in range(10):
        if dp[i][t][7]:
            print(t)
            exit()

print(-1)
