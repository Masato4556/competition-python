from collections import defaultdict
import heapq
from functools import lru_cache
import sys
sys.setrecursionlimit(10 ** 9)


N = int(input())

G = [set() for _ in range(N)]
degs = [0 for _ in range(N)]
for _ in range(N-1):
    u, v = map(lambda x: int(x)-1, input().split())
    G[u].add(v)
    G[v].add(u)
    degs[u] += 1
    degs[v] += 1


count_1 = 0
count_2 = 0
count_othsers = defaultdict(int)
for i in range(N):
    if degs[i] == 1:
        count_1 += 1
    elif degs[i] == 2:
        count_2 += 1
    else:
        count_othsers[degs[i]] += 1


total_k = 0
num = 0
for k, v in count_othsers.items():
    total_k += k*v
    num += 1

if num > 0:
    count_1 += (num-1) * 2
    count_2 -= (num-1) * 2

while count_2 > 0:
    if count_1 == count_2 * 2 + total_k:
        break
    count_1 += 2
    count_2 -= 2

ans = []
for i in range(count_2):
    ans.append(2)

for k, v in count_othsers.items():
    for _ in range(v):
        ans.append(k)

ans.sort()
print(*ans)
