
import heapq
import time

time_sta = time.perf_counter()

N, K = map(int, input().split())
A = list(map(int, input().split()))


def f(l, r):
    ret = []
    for i in range(N):
        if l <= i <= r:
            ret.append(A[r+l-i])
        else:
            ret.append(A[i])
    return ret


l = [0] * N
m = [0] * N

cc = list(range(1, N+1))

for i in range(N):
    cc.remove(A[i])
    for a_j in cc:
        if A[i] < a_j:
            m[i] += 1
        else:
            l[i] += 1

sum_l = sum(l)
sum_m = sum(m)

if K <= sum_l:
    ans = []
    cnt = 0
    start = 0
    for i in range(N):
        if cnt + l[i] > K:
            start = i
            break
        cnt += l[i]
    for j in range(start + 1, N):
        if A[start] < A[j]:
            continue
        ans.append(f(start, j))
    ans.sort()
    print(*ans[K-cnt-1])

elif K <= sum_l + N:
    print(*A)
else:
    ans = []
    cnt = sum_l + N
    start = 0
    for i in range(N-1, -1, -1):
        if cnt + m[i] > K:
            start = i
            break
        cnt += m[i]
    AA = []
    for j in range(start + 1, N):
        if A[start] > A[j]:
            continue
        ans.append(f(start, j))
        heapq.heappush(AA, (A[j], j))
    for _ in range(K-cnt+1):
        v, end = AA.pop()
    print(*f(start, end))
