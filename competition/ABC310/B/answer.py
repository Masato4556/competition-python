
N, M = map(int, input().split())

items = []
for _ in range(N):
    P, C, *F = list(map(int, input().split()))
    items.append([P, C, set(F)])

items.sort(reverse=True)
# print(items)

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if items[i][0] < items[j][0]:
            continue
        elif items[i][0] == items[j][0]:
            if items[i][1] >= items[j][1]:
                continue
        flg = True
        for f in items[i][2]:
            if f not in items[j][2]:
                flg = False
                break
        if flg:
            print("Yes")
            exit()
print("No")
