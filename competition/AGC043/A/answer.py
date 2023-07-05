INF = 10**3
H, W = map(int, input().split())

S = [input() for _ in range(H)]


dp = [[INF for _ in range(W)] for _ in range(H)]

for y in range(H):
    for x in range(W):
        if x == 0 and y == 0:
            dp[0][0] = 1 if S[0][0] == "#" else 0
        if y - 1 >= 0:
            temp = dp[y-1][x]
            if S[y-1][x] == "." and S[y][x] == "#":
                temp += 1
            dp[y][x] = min(dp[y][x], temp)
        if x - 1 >= 0:
            temp = dp[y][x-1]
            if S[y][x-1] == "." and S[y][x] == "#":
                temp += 1
            dp[y][x] = min(dp[y][x], temp)

print(dp[-1][-1])
