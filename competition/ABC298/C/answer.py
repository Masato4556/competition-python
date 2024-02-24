import heapq
from collections import defaultdict

N = int(input())
Q = int(input())

include = defaultdict(set)
ans2 = [list() for _ in range(N+1)]
ans3 = defaultdict(list)
for _ in range(Q):
    query = list(map(int, input().strip().split()))
    if query[0] == 1:
        i, j = query[1], query[2]
        heapq.heappush(ans2[j], i)
        if j not in include[i]:
            include[i].add(j)
            heapq.heappush(ans3[i], j)
    elif query[0] == 2:
        temp = []
        for _ in range(len(ans2[query[1]])):
            temp.append(heapq.heappop(ans2[query[1]]))
        print(*temp)
        ans2[query[1]] = temp
    else:
        temp = []
        for _ in range(len(ans3[query[1]])):
            temp.append(heapq.heappop(ans3[query[1]]))
        print(*temp)
        ans3[query[1]] = temp
