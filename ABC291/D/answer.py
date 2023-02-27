from collections import defaultdict
n = int(input())

cards = []
for _ in range(n):
    a, b = map(int, input().split())
    cards.append([a, b])

dp = [[0, 0] for _ in range(n)]
dp[0] = [1, 1]

for i in range(1, n):
    for prev in range(2):
        prev_num = cards[i-1][prev]
        for curr in range(2):
            curr_num = cards[i][curr]
            if prev_num == curr_num: continue

            dp[i][curr] +=  dp[i-1][prev]
    dp[i][0] %= 998244353  
    dp[i][1] %= 998244353 

print((dp[-1][0] + dp[-1][1]) % 998244353)
