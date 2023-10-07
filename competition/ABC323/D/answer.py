import heapq

N = int(input())
slime_nums = dict()
slime_size_que = []


for i in range(N):
    s, c = map(int, input().split())
    slime_nums[s] = c
    heapq.heappush(slime_size_que, s)


ans = 0
while len(slime_size_que) > 0:
    s = heapq.heappop(slime_size_que)
    c = slime_nums[s]

    ans += c % 2

    next_size = s*2
    next_num = c//2
    if next_num > 0:
        if next_size not in slime_nums:
            slime_nums[next_size] = next_num
            if next_num >= 2:
                heapq.heappush(slime_size_que, next_size)
            else:
                ans += 1
        else:
            slime_nums[next_size] += next_num

print(ans)
