n = int(input())

l, r, u, d = 1, n, 1, n

while True:
    print("? {} {} {} {}".format(l, (l+r-1) // 2, 1, n))
    expected_num = (l+r-1) // 2 - (l - 1)
    num = int(input())

    if num < expected_num:
        r = (l+r-1) // 2
    else:
        l = (l+r-1) // 2 + 1

    if l == r: break

while True:
    print("? {} {} {} {}".format(1, n, u, (u+d-1) // 2))
    expected_num = (u+d-1) // 2 - (u - 1)
    num = int(input())
    
    if num < expected_num:
        d = (u+d-1) // 2
    else:
        u = (u+d-1) // 2 + 1

    if u == d: break

print("! {} {}".format(l, u))
