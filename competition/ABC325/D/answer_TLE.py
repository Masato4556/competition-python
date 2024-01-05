import heapq
N = int(input())

que = []
printed = [0] * N

bins = set()
for i in range(N):
    t, q = map(int, input().split())
    heapq.heappush(que, (t+q, t, i))
    bins.add(t)
    bins.add(t+q)

bins = list(bins)
bins.sort()

# print(bins)
current = 0
for bin in bins:
    printable_count = bin - current
    current = bin

    temp = []
    while len(que) > 0 and printable_count > 0:
        q, t, i = heapq.heappop(que)
        if t <= bin <= q:  # printable
            printed[i] = 1
            printable_count -= 1
            break
        else:
            if q > bin:
                temp.append((q, t, i))

    for v in temp:
        heapq.heappush(que, v)

print(sum(printed))
