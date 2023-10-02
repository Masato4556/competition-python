N, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
s = sum(A)

if s-A[-1] >= X:
    print(0)
    exit()

ans = X - (s-A[0]-A[-1])
if A[0] <= ans <= A[-1]:
    print(ans)
else:
    print(-1)
# print(s)
# print(X - (s-A[0]-A[-1]))
