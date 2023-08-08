
N = int(input())
A = list(map(int, input().split()))


t = sum(A)//N

if sum(A) == t * N:
    ans = 0
    for i in range(N):
        if A[i] < t:
            ans += t - A[i]
    print(ans)
    exit()

ans1 = 0
ans2 = 0
for i in range(N):
    if A[i] < t:
        ans1 += t - A[i]
for i in range(N):
    if A[i] > t+1:
        ans2 += A[i] - (t+1)

print(max(ans1, ans2))
