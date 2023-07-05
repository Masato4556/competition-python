import heapq

N, K = map(int, input().split())
S = list(input())

x_num = S.count("X")

if x_num < K:
    S = ["Y" if s == "X" else "X" for s in S]
    K = N - K

x_num = S.count("X")

if x_num == N:
    print(K-1 if K != 0 else 0)
    exit()

x_cnt, y_cnt = 0, 0
x_nums, y_nums = [], []

if S[0] == "X": y_nums.append(0)

for i in range(N):
    if S[i] == "X":
        x_cnt += 1
        if y_cnt > 0:
            y_nums.append(y_cnt)
            y_cnt = 0
    else:
        y_cnt += 1
        if x_cnt > 0:
            x_nums.append(x_cnt)
            x_cnt = 0

if x_cnt > 0: x_nums.append(x_cnt)
if y_cnt > 0: y_nums.append(y_cnt)

if S[-1] == "X": y_nums.append(0)

c = []
for i in range(len(x_nums)):
    add = -1 + int(y_nums[i] > 0) + int(y_nums[i+1] > 0)
    heapq.heappush(c, (add * -1, x_nums[i]))


ans = sum([y_num - 1 for y_num in y_nums if y_num > 0])
while len(c):
    add, cost = heapq.heappop(c)
    add *= -1
    if cost <= K:
        ans += cost + add
        K -= cost
ans += K
print(ans)

