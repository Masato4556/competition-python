
import heapq
N = int(input())
A = list(map(int, input().split()))

A_sum = sum(A)
if A_sum % N != 0:
    print("No")
    exit()


print("Yes")
base = A_sum // N
diff = 0

aa = sum(range(1, N+1)) / N
ff = 0
for i in range(N):
    if A[i] - base > 0: diff += A[i] - base
    if i+1 - aa > 0: ff += i+1 - aa

M = round(diff / ff)
print(M)

cr = []
for ind, a in enumerate(A):
    heapq.heappush(cr, (a, ind))
    
nx = []
for i in range(M):
    ans = [0] * N
    for i in range(N):
        v, ind = heapq.heappop(cr)
        ans[ind] = str(N-i)
        heapq.heappush(nx, (v + N - i, ind))
    print(" ".join(ans))
    cr = nx
    nx = []