N = int(input())
A = list(map(int, input().split()))

dp_l = [0] * N
dp_l[0] = 1

dp_r = [0] * N
dp_r[N-1] = 1

for i in range(1, N):
    dp_l[i] = min(dp_l[i-1]+1, A[i])
    dp_r[N-1-i] = min(dp_r[N-i]+1, A[N-i-1])

# print(dp_l)
# print(dp_r)

print(max([min(dp_l[i], dp_r[i]) for i in range(N)]))
