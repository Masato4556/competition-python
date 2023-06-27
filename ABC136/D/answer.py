
S = input()
length = len(S)

i = 0
ans = []
while i < length:
    rc = 0
    lc = 0
    while i < length and S[i] == "R":
        rc += 1
        i += 1
    while i < length and S[i] == "L":
        lc += 1
        i += 1

    for j in range(rc + lc):
        if j != rc - 1 and j != rc:
            ans.append(0)
            continue

        if j == rc-1:
            if (rc + lc) % 2 != 0 and rc % 2 != 0:
                ans.append((rc + lc) // 2 + 1)
            else:
                ans.append((rc + lc) // 2)
            continue

        ans.append((rc + lc) - ans[-1])

print(*ans)
