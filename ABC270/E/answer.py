import heapq
import copy

n, k = map(int, input().split())
A = list(map(int, input().split()))
res = A.copy()

heapq.heapify(A)

loop = 0
not_zero_len = n
prev_A_min = 0
for i in range(n):
    a_min = heapq.heappop(A)
    eat_num = (a_min - prev_A_min) * not_zero_len
    if k < eat_num : 
        break
    
    k -= eat_num
    loop += a_min - prev_A_min
    not_zero_len -= 1
    prev_A_min = a_min

if not_zero_len == 0:
    print(*[0]*n)
    exit()

loop += k // (not_zero_len)
k %= not_zero_len

for i in range(n):
    res[i] = max(0, res[i] - loop)
    if res[i] > 0 and k > 0:
        res[i] -= 1
        k -= 1

print(*res)
