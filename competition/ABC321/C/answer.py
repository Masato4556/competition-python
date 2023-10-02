from math import comb
from itertools import combinations

k = int(input())
k += 1

digit = 0
for i in range(1, 11):
    c = comb(10, i)
    if k <= comb(10, i):
        digit = i
        break
    k -= c

l = list(combinations(range(9, -1, -1), digit))
l.reverse()

ans = [str(v) for v in l[k-1]]
print("".join(ans))
