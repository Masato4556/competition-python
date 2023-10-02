N, M = map(int, input().split())
A = list(map(lambda x: int(x)-1, input().split()))

ans = [0] * N

a_i = M-1
day_num = 0
for i in range(N-1, -1, -1):
    day_num += 1

    if a_i >= 0 and i == A[a_i]:
        day_num = 0
        a_i -= 1

    ans[i] = day_num

for a in ans:
    print(a)
