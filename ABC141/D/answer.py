import heapq
N, M = map(int, input().split())
A = list(map(lambda x: int(x) * -1, input().split()))

heapq.heapify(A)

ans = 0
while len(A):
    v = heapq.heappop(A)
    v *= -1

    if M > 0:
        M -= 1
        v //= 2
        heapq.heappush(A, -1 * v)
    else:
        ans += v

print(ans)