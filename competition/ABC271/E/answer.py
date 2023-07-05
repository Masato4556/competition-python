# 参考 https://atcoder.jp/contests/abc271/submissions/39095596
# ベルマン・フォード法の亜種みたいな感じ？

INF = 10**18 + 1

n, m, k = map(int, input().split())

routes = []
for i in range(m):
    a, b, c = map(int, input().split())
    routes.append((a-1, b-1, c))

E = list(map(lambda x: int(x) - 1, input().split()))

dp = [INF] * n
dp[0] = 0

# 数列Eの順番で更新を行う
for e in E:
    a, b, c = routes[e]
    dp[b] = min(dp[b], dp[a] + c)

print(dp[-1] if dp[-1] != INF else -1)
