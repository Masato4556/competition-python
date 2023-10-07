import heapq
from collections import defaultdict

N = int(input())
slime_nums = defaultdict(int)
slime_size_que = []
slime_size_set = set()


for i in range(N):
    s, c = map(int, input().split())
    slime_nums[s] = c
    heapq.heappush(slime_size_que, s)
    slime_size_set.add(s)


ans = 0
while len(slime_size_que) > 0:
    s = heapq.heappop(slime_size_que)
    c = slime_nums[s]

    ans += c % 2

    next_size = s*2
    next_num = c//2
    if next_num > 0:
        slime_nums[next_size] += next_num
        if next_size not in slime_size_set:
            if len(slime_size_que) == 0 or next_size > slime_size_que[-1]*2:
                while next_num > 0:
                    ans += next_num % 2
                    next_num //= 2
            else:
                heapq.heappush(slime_size_que, next_size)
                slime_size_set.add(next_size)

print(ans)
