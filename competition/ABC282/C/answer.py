
n = int(input())
s = input()

cnt = 0
ans = []
for c in s:
    if c == "\"":
        cnt += 1
    elif c == ",":
        if cnt % 2 == 0:
            ans.append(".")
            continue
    ans.append(c)

print("".join(ans))
