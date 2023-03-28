from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

AM = defaultdict(int) 
A.sort(reverse=True)
ans = sum(A)

start_inds = set()

for i in range(N):
    ii = A[i] % M
    AM[ii] += A[i]

    if (ii-1) % M in AM:
        start_inds.discard(ii) 
    else:
        start_inds.add(ii)
        
        
    if ((ii+1) % M) in start_inds:
        start_inds.discard((ii+1) % M)

if len(start_inds) == 0:
    print(0)
    exit()


played_sum_max = 0
for i in start_inds:
    played_sum = 0
    for ii in range(i, i+M):
        if (ii % M) not in AM: break
        played_sum += AM[ii % M]

    played_sum_max = max(played_sum_max, played_sum)

print(sum(A) - played_sum_max)