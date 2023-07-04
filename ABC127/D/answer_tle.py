
import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))

heapq.heapify(A)

for _ in range(M):
    b, c = map(int, input().split())

    for _ in range(b):
        if A[0] >= c:
            break
        heapq.heappushpop(A, c)

print(sum(A))
