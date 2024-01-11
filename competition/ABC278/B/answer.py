
H, M = map(int, input().split())

while True:
    h = str(H).zfill(2)
    m = str(M).zfill(2)

    if "00" <= h[0]+m[0] < "24" and "00" <= h[1]+m[1] < "59":
        print(H, M)
        break

    M += 1
    if M == 60:
        H += 1
        M = 0
    if H == 24:
        H = 0
