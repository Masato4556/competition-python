import heapq
N, M = map(int, input().split())
P = list(map(int, input().split()))
P.sort()

L = list(map(int, input().split()))
D = list(map(int, input().split()))
V = [(l, -1 * d) for l, d in zip(L, D)]
heapq.heapify(V)

availables = []

ans = 0

for i in range(N):
    while len(V) > 0 and P[i] >= V[0][0]:
        _, d = heapq.heappop(V)
        heapq.heappush(availables, d)
    
    ans += P[i]
    if len(availables) > 0:
        ans += heapq.heappop(availables)
    
print(ans)
