x, y, z = map(int, input().split())

if (abs(x) < abs(y)) or (x * y < 0):
    print(abs(x))
    exit()

if (abs(z) < abs(y)) or (z * y < 0):
    print(abs(z) + abs(x-z))
    exit()

print(-1)