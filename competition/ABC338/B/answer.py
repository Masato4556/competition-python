from collections import defaultdict
S = list(input())

S.sort()

max_count = 0
count = defaultdict(int)
ans = ""
for c in S:
    count[c] += 1
    if count[c] > max_count:
        max_count = count[c]
        ans = c

print(ans)
