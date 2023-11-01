N, M = map(int, input().split())
A = list(map(int, input().split()))

S = [0] * (N-M+1)
S[0] = sum(A[0:M])
for i in range(N-M):
    S[i+1] = S[i] - A[i] + A[i+M]

cur = 0

for i in range(M):
    cur += (i+1) * A[i]
ans = cur

for i in range(N-M):
    cur += M * A[i+M] - S[i]
    if cur > ans:
        ans = cur
print(ans)