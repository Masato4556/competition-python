N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

pairs = set()

for i in range(M):
    for j in range(N-1):
        a1 = min(A[i][j], A[i][j+1])
        a2 = max(A[i][j], A[i][j+1])
        pairs.add((a1, a2))

ans = 0
for i in range(1, N+1):
    for j in range(i+1, N+1):
        if (i, j) not in pairs:
            ans += 1


print(ans)
