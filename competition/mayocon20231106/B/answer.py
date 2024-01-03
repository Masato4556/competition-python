from collections import defaultdict

N, Q = map(int, input().split())
A = list(map(int, input().split()))

counter = defaultdict(int)
d = dict()
for i, a in enumerate(A):
    counter[a] += 1
    d[(a, counter[a])] = i + 1

for _ in range(Q):
    x, k = map(int, input().split())
    if (x, k) in d:
        print(d[(x, k)])
    else:
        print(-1)
