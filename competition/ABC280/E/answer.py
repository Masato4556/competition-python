# WA
# これでも解けそうな気がするけど、なぜ解けないのだろう
# → ans += と書くところを ans =　としてしまっていただけだった。。。
#
# 上記の点を直してもTLE
# 下記の自分の回答では２次元のDP（p回目の攻撃で、残りHPがqになっている確率）を用いているが、
# 解説では１次元のDP(モンスターの体力がpの時の、攻撃回数の期待値)を用いており、こちらの方が当然計算量が小さい

from collections import defaultdict

MOD = 998244353
denominator = pow(100, MOD - 2, MOD) # atcoderのPyPy3 だと pow(100, -1, MOD)は使えない

N, P = map(int, input().split())

dp = [defaultdict(int) for _ in range(N+1)]
dp[0][N] = 1

for i in range(N):
    for prev_damage, prev_p in dp[i].items():
        if prev_damage != 0:
            dp[i+1][max(prev_damage-2, 0)] += prev_p * P * denominator % MOD
            dp[i+1][max(prev_damage-1, 0)] += prev_p * (100-P) * denominator % MOD

ans = 0 
for i in range(1, N+1):
    ans += dp[i][0] * i % MOD
print(ans % MOD)
