
n = int(input())
A = list(map(int, input().split()))

called = set()
for i in range(n):
    if i in called: continue
    called.add(A[i]-1)

ans = [i+1 for i in range(n) if i not in called]
print(len(ans))
print(*ans)
