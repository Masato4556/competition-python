import heapq

N = int(input())
P = list(map(int, input().split()))

q = []
prev = 1000

for i in range(N-1, -1, -1):
    pi = P[i]
    if pi > prev:
        break
    heapq.heappush(q, pi)
    prev = pi

fixedP = []
target = P[i]
for j in range(i):
    fixedP.append(P[j])

head = 0
temp = []
for i in range(len(q)):
    p = heapq.heappop(q)
    temp.append(p)
    if p > target:
        break
    head = p

for t in temp:
    heapq.heappush(q, t)

heapq.heappush(q, target)

dec = []
while len(q):
    p = heapq.heappop(q)
    if p == head:
        continue
    dec.append(p)

dec.reverse()

ans = []
ans.extend(fixedP)
ans.append(head)
ans.extend(dec)

print(*ans)
    
 