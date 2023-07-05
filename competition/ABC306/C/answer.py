
N = int(input())
A = list(map(int, input().split()))
cnt = [0 for _ in range(N)]

ans = []
for i in range(N * 3):
    cnt[A[i]-1] += 1
    if cnt[A[i]-1] == 2:
        ans.append(A[i])
print(*ans)
