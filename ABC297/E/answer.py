import heapq
N, K = map(int, input().split())
A = list(set(map(int, input().split())))
A_num = len(A)

costs = [a for a in A]
heapq.heapify(costs)


fixed_costs = []
costs_set = set(costs)
for _ in range(K):
    a = heapq.heappop(costs)
    heapq.heappush(fixed_costs, a)

    for i in range(A_num):
        if a + A[i] in costs_set: continue
        heapq.heappush(costs, a + A[i])
        costs_set.add(a + A[i])

print(fixed_costs[K-1])
