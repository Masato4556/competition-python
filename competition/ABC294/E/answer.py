L, N1, N2 = map(int, input().split())

V1 = [list(map(int, input().split())) for _ in range(N1)]
V2 = [list(map(int, input().split())) for _ in range(N2)]

i1 = 0
i2 = 0

cnt = 0
while True:
    if i1 >= N1 and i2 >= N2:
        break

    v1 = V1[i1]
    v2 = V2[i2]

    if v1[1] > v2[1]:
        c = v2[1]
        v1[1] -= v2[1]
        i2 += 1
    elif v1[1] < v2[1]:
        c = v1[1]
        v2[1] -= v1[1]
        i1 += 1
    else:
        c = v1[1]
        i1 += 1
        i2 += 1

    if v1[0] == v2[0]:
        cnt += c

print(cnt)