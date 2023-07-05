
import heapq
N = int(input())
A = list(map(int, input().split()))

A_sum = sum(A)
if A_sum % N != 0:
    print("No")
    exit()


base = A_sum // N
diff = 0

aa = sum(range(1, N+1)) / N
ff = 0
for i in range(N):
    if A[i] - base > 0: diff += A[i] - base
    if i+1 - aa > 0: ff += i+1 - aa

cr = []
for ind, a in enumerate(A):
    heapq.heappush(cr, (a, ind))

cnt = 0
ans_list = []
nx = []
for i in range(1000):
    cnt += 1
    ans = [0] * N
    finish = True
    flg = True
    for i in range(N):
        v, ind = heapq.heappop(cr)
        ans[ind] = str(N-i)
        heapq.heappush(nx, (v + N - i, ind))
        if flg:
            p = v + N - i
            flg = False
        elif v + N - i != p: finish = False
    ans_list.append(" ".join(ans))
    cr = nx
    nx = []
    if finish: break
    if cnt > 20: break

for i in range(1, N):
    if cr[i][0] != cr[0][0]:
        print("No")
        exit()

print("Yes")
print(cnt)
print("\n".join(ans_list))
