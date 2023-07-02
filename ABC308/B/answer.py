from collections import defaultdict
N, M = map(int, input().split())

C = input().split()
D = input().split()
P = list(map(int, input().split()))

prices = defaultdict(lambda: P[0])
for i in range(M):
    prices[D[i]] = P[i+1]

ans = 0
for i in range(N):
    ans += prices[C[i]]
print(ans)
