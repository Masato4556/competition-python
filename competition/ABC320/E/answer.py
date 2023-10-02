import heapq


N, M = map(int, input().split())

events = []
for _ in range(M):
    t, w, s = map(int, input().split())
    heapq.heappush(events, (t, 2, w, s))

exists = list(range(N))
ans = [0 for _ in range(N)]

while len(events):
    t, k, a, b = heapq.heappop(events)
    if k == 2:
        if not len(exists):
            continue
        i = heapq.heappop(exists)
        ans[i] += a
        heapq.heappush(events, (t+b, 1, i, -1))
    else:
        heapq.heappush(exists, a)

for a in ans:
    print(a)
