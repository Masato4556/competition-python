from math import floor, ceil
import heapq

N = int(input())

que = [-N]

ans = 0
while que:
    x = heapq.heappop(que)
    x *= -1

    if x == 1:
        print(ans)
        exit()

    ans += x
    que.append(-1 * floor(x/2))
    que.append(-1 * ceil(x/2))
