from itertools import groupby
import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

AA = [(-1 * k, len(list(g))) for k,g in groupby(A)]


for _ in range(M):
    b, c = map(int, input().split())
    heapq.heappush(AA, (-1 * c, b))


cnt = 0 
ans = 0
while cnt < N:
    v, n = heapq.heappop(AA)
    v *= -1
    if cnt + n > N:
        ans += v * (N - cnt)
        break
    else:
        ans += v * n
        cnt += n


print(ans)

