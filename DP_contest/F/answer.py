# 解説　https://kyopro-friends.hatenablog.com/entry/2019/01/12/231000

# pythonの解答例
# https://wakabame.hatenablog.com/entry/2019/02/10/012106#:~:text=print(ans)-,F%20%2D%20LCS,-atcoder.jp

s = input()
t = input()

# sをi文字目、tをj文字目まで使って作れる部分列の最長の長さをdpに格納する
dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
for i in range(1,  len(s)+1):
    for j in range(1, len(t)+1):
        # - sのi文字目とtのj文字が同じ場合、その文字を部分列に含めるため、dp[i-1][j-1]より1大きい値で更新する
        # - sのi文字目とtのj文字が同じでない場合、一つ前の長さより大きくなることはないため、dp[i-1][j](sの1文字前)とdp[i][j-1](jの一文字前)のうち大きい方で更新する
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + (s[i-1] == t[j-1]))

# DP復元
# dp[i][j] != dp[i-1][j] かつ dp[i][j] != dp[i][j-1]の場合、s[i](t[j])の文字を加えることで、部分列の長さが大きくなったことがわかる。
# そのような文字列をdpの末尾から探していくことで、文字列を復元できる

ans = []
x = len(s)
y = len(t)
while x > 0 and y > 0:
    if dp[x][y] == dp[x-1][y]: x -= 1
    elif dp[x][y] == dp[x][y-1]: y -= 1
    else:
        x -= 1
        y -= 1
        ans += s[x]
ans.reverse()
print("".join(ans))