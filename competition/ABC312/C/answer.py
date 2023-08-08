import heapq
N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

que = []
for a in A:
    heapq.heappush(que, (a, "A"))

for b in B:
    heapq.heappush(que, (b+1, "B"))

a_cnt, b_cnt = 0, M
while len(que):
    v, mode = heapq.heappop(que)

    if mode == "A":
        a_cnt += 1
    else:
        b_cnt -= 1
    ans = v

    if a_cnt >= b_cnt:
        print(ans)
        exit()
