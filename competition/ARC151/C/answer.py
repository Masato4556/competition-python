from collections import defaultdict
N = int(input())

A = defaultdict(int)
for a in map(int, input().split()):
    A[a] += 1

print(A)
