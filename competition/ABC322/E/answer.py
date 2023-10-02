from collections import defaultdict
disable = 10**16

N, K, P = map(int, input().split())

devs = []
for _ in range(N):
    c, *a = map(int, input().split())
    devs.append((c, a))
# print(devs)
dp = [defaultdict(lambda: disable) for _ in range(N+1)]
dp[0][tuple(0 for _ in range(K))] = 0

for i in range(N):
    c, a = devs[i]

    d_cp = dp[i].copy()
    for prev_ks, prev_c in d_cp.items():
        cur_ks = tuple(min(k+a, P) for k, a in zip(list(prev_ks), a))
        dp[i+1][prev_ks] = min(prev_c, dp[i+1][prev_ks])
        dp[i+1][cur_ks] = min(prev_c + c, dp[i+1][cur_ks])


print(dp[-1][tuple(5 for _ in range(K))] if dp[-1]
      [tuple(5 for _ in range(K))] != disable else -1)
