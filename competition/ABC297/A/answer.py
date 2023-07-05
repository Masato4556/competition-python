N, D = map(int, input().split())

prev = -10**12
for t in map(int, input().split()):
    if t - prev <= D:
        print(t)
        exit()
    prev = t

print(-1)
