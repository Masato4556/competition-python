
N = int(input())

P = list(map(int, input().split()))

ans = 0
for i in range(1, N):
    if P[0] <= P[i]:
        ans = max(ans, P[i] - P[0] + 1)
print(ans)
