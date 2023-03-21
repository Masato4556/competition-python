import heapq
from collections import deque
N, Q = map(int, input().split())

events = [list(map(int, input().split())) for _ in range(Q)]

nums = deque([i+1 for i in range(N)])
called_nums = []
visited_nums = set()

for e in events:
    if e[0] == 1:
        if len(nums) == 0: continue
        heapq.heappush(called_nums, nums.popleft())
    elif e[0] == 2:
        visited_nums.add(e[1])
    else:
        while len(called_nums):
            if called_nums[0] not in visited_nums:
                print(called_nums[0])
                break
            heapq.heappop(called_nums)
