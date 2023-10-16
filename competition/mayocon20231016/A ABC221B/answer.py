s = input()
t = input()

if s == t:
    print("Yes")
    exit()

for i in range(len(s)-1):
    flg = True
    for j in range(len(s)):
        if j == i:
            if s[j] == t[i+1]:
                continue
        elif j == i+1:
            if s[j] == t[i]:
                continue

        if s[j] == t[j]:
            continue

        flg = False
        break

    if flg:
        print("Yes")
        exit()

print("No")
