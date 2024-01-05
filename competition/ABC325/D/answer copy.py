import heapq
N = int(input())

que = []
ans = 0

bins = set()
printable_priducts = dict()
for i in range(N):
    t, q = map(int, input().split())
    if t not in printable_priducts:
        printable_priducts[t] = []
    printable_priducts[t].append((t+q, t))

    # (時間、タイプ)
    # タイプ0: その時間に印刷可能になる商品をキューに追加する
    # タイプ1: その時間までに印刷可能な商品に可能な限り印刷を行う
    bins.add((t, 0))
    bins.add((t-1, 1))
    bins.add((t+q, 1))

bins = list(bins)
bins.sort()

prev = 0
for bin, type in bins:
    if type == 0:
        for product in printable_priducts[bin]:
            heapq.heappush(que, product)
        continue

    printable_count = bin - prev
    prev = bin

    while len(que) > 0 and printable_count > 0:
        q, t = heapq.heappop(que)
        if bin <= q:  # printable
            ans += 1
            printable_count -= 1
print(ans)
