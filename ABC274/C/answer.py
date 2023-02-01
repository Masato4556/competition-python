from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))
uniq_A = list(set(A))
uniq_A.sort()
l = len(uniq_A)
result = defaultdict(int)

for i in range(n):
    result[l - (uniq_A.index(A[i]) + 1)] += 1

for i in range(n):
    if i > l:
        print(0)
        continue
    print(result[i])
