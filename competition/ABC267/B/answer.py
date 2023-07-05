s = input()

if s[0] == "1":
    print("No")
    exit()

ans = "No"
res = []
for line in [[7], [4], [2, 8], [1, 5], [3, 9], [6], [10]]:
    all_0 = True
    for p in line:
        if s[p-1] == "1":
            all_0 = False
            break

    if len(res) == 0 and all_0 == False:
        res.append(all_0)
        continue

    if len(res) > 0 and res[-1] != all_0:
        res.append(all_0)

print("Yes" if len(res) > 2 else "No")