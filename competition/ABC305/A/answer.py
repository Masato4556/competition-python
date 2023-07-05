
N = int(input())


if N % 5 >= 3:
    print((N // 5 + 1) * 5)
    exit()
else:
    print((N // 5) * 5)
    exit()
