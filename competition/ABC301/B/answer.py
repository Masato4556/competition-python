
N = int(input())

A = list(map(int, input().split()))

ans = []
for i in range(N-1):
    a1, a2 = A[i], A[i+1]
    if abs(a1 - a2) <= 1:
        ans.append(str(a1))
        continue
    for a in range(a1, a2, 1 if a1 < a2 else -1):
        ans.append(str(a))

ans.append(str(A[-1]))
print(" ".join(ans))
