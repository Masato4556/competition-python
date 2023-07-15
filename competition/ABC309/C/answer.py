
N, K = map(int, input().split())

AB_ = [list(map(int, input().split())) for _ in range(N)]

AB_.sort(reverse=True)

AB = []
prev_a = -1
for i in range(N):
    a, b = AB_[i]
    if a != prev_a:
        AB.append([a, b])
    else:
        AB[-1][1] += b
    prev_a = a

cnt = 0
for i in range(N):
    a, b = AB[i]
    cnt += b
    if cnt > K and a != prev_a:
        print(a+1)
        exit()

print(1)
