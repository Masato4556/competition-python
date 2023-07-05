from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))
A.sort()
l = len(A)
r = [0 for _ in range(n)]

prev = -1
p = -1
for i in range(n):
    curr = A[l - 1 - i]
    if curr == prev:
        r[p] += 1
        continue

    p += 1
    r[p] += 1
    prev = curr

print("\n".join(list(map(str, r))))

