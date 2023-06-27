import heapq
from collections import defaultdict

N, K, Q = map(int, input().split())

A = [0] * N
B = [0] * N
erase = defaultdict(int)
for i in range(Q):
    x, y = map(int, input().split())
    x -= 1

    erase[A[x]] += 1
    A[x] = y
    heapq.heappush(B, -1 * y)

    temp = []
    cnt = 0
    ans = 0
    while len(B):
        v = heapq.heappop(B) * -1
        if erase[v] > 0:
            erase[v] -= 1
            continue
        if cnt < K:
            ans += v
        temp.append(v)
        cnt += 1
    print(ans)

    for v in temp:
        heapq.heappush(B, -1 * v)
