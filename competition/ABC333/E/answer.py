from collections import deque, defaultdict
N = int(input())
events = [tuple(map(int, input().split())) for _ in range(N)]

events.reverse()

que = deque()
counter = defaultdict(int)
ans = []
for t, x in events:
    if t == 2:
        que.append((t, x))
        counter[x] += 1
    else:
        if counter[x] > 0:
            que.append((t, x))
            counter[x] -= 1
            ans.append(1)
        else:
            ans.append(0)

if sum([count for count in counter.values()]) != 0:
    print(-1)
    exit()

ss = set()
portion_counter = defaultdict(int)
K_min = 0
k = 0
while que:
    t, v = que.pop()
    if t == 1:
        k += 1
    else:
        k -= 1

    K_min = max(K_min, k)

print(K_min)
ans.reverse()
print(*ans)
