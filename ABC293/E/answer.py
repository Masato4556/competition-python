
a, x, m = map(int, input().split())

t = 1
cnt = 1
bb = 1
while True:
    t *= a
    t % m
    print(t, t % m)
    if t % m == 1 : break
    cnt += 1
    bb += t % m

print(cnt, bb)