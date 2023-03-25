from collections import defaultdict
N = int(input())

A = defaultdict(int)
for a in map(int, input().split()):
    A[a] += 1

ans = 0
for v in A.values():
    ans += v // 2
print(ans)