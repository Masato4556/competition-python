import heapq

N, D, P = map(int, input().split())
F = list(map(lambda x: -1*int(x), input().split()))

heapq.heapify(F)

ans = 0
d_total = 0
cnt = 0
while len(F):
    f = -1 * heapq.heappop(F)
    cnt += 1
    d_total += f
    if cnt == D:
        ans += min(d_total, P)
        cnt = 0
        d_total = 0
ans += min(d_total, P)

print(ans)
