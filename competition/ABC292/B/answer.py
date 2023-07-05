
n, q = map(int, input().split())

events = [list(map(int, input().split())) for _ in range(q)]
res = [0] * n

for e in events:
    if e[0] == 1:
        res[e[1]-1] += 1
    elif  e[0] == 2:
        res[e[1]-1] += 2
    else:
        print("Yes" if res[e[1]-1] >= 2 else "No")
