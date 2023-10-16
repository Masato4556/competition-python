import heapq
N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

que = []
que.append((-A[0], A[0]))
# print(A)
# print(que)
ans = 0
for i in range(1, N):
    a = A[i]
    low_side, high_side = heapq.heappop(que)
    low_side *= -1
    ans += low_side

    heapq.heappush(que, (-a, low_side))
    heapq.heappush(que, (-a, high_side))
    # print(que)

print(ans)
