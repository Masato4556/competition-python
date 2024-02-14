from collections import defaultdict
N = int(input())
S = input().strip()

counter = defaultdict(int)
prev = ''
cnt = 0
for c in S:
    if c != prev:
        counter[prev] = max(counter[prev], cnt)
        prev = c
        cnt = 1
        continue

    cnt += 1

counter[prev] = max(counter[prev], cnt)
del counter[""]


ans = 0
for v in counter.values():
    ans += v
print(ans)