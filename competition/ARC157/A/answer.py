N, A, B, C, D = map(int, input().split())

if B + C == 0 and A * D > 0:
    print("No")
    exit()

if abs(B-C) > 1:
    print("No")
    exit()

print("Yes")