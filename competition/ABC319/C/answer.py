from itertools import permutations
from math import factorial
C = []
for _ in range(3):
    C.extend(list(map(int, input().split())))

lines = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]

cnt = 0
for p in permutations(range(9)):
    order = {p[i]: i for i in p}
    for a, b, c in lines:
        if C[a] == C[b] and order[a] < order[c] and order[b] < order[c]:
            cnt += 1
            break
        if C[b] == C[c] and order[b] < order[a] and order[c] < order[a]:
            cnt += 1
            break
        if C[c] == C[a] and order[c] < order[b] and order[a] < order[b]:
            cnt += 1
            break
total = factorial(9)
print((total-cnt)/total)
