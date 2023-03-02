from math import ceil

n, m = map(int, input().split())
A = list(map(int, input().split()))

nums = [set() for _ in range(m)]

# p回目にAiが、
for i in range(n):
    if A[i] >= n: continue

    p = 1
    if A[i] < 0:
        p = ceil(-1 * A[i] / (i+1))

    aa = A[i] + p * (i + 1)
    while aa < n and p <= m:
        nums[p-1].add(aa % n)
        p += 1
        aa += (i+1)

for i in range(m):
    for j in range(n+1): # 0~nまでのうち、numsに含まれない最も小さい数値をprintする
        if j not in nums[i]: 
            print(j)
            break

