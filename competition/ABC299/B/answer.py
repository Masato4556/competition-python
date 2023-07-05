from collections import defaultdict
N, T = map(int, input().split())

C = []
C_set =set()
for i, c in enumerate(map(int, input().split())):
    if i == 0:
        first_c = c
    C.append(c)
    C_set.add(c)

target_c = T
if T not in C_set:
    target_c = first_c

max_r = -1
ans = -1
for i, r in enumerate(map(int, input().split())):
    if C[i] == target_c and r > max_r:
        max_r = r
        ans = i + 1

print(ans)