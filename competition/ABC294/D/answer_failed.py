from collections import deque
N, Q = map(int, input().split())

events = [list(map(int, input().split())) for _ in range(Q)]

nums = deque([i+1 for i in range(N)])
called_nums = deque([])

for e in events:
    if e[0] == 1:
        if len(nums) == 0: continue
        called_nums.append(nums.popleft())
    elif e[0] == 2:
        called_nums.remove(e[1])
    else:
        if len(called_nums) == 0: continue
        print(called_nums[0])