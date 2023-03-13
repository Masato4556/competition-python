
t = int(input())
for _ in range(t):
    x = list(map(int, input().split()))
    a = [0, 2, 4]

    x.sort()
    d1, d2 = min(x[2] - x[1], x[1] - x[0]), max(x[2] - x[1], x[1] - x[0])

    if d1 % 2 != 0 or d2 % 2 != 0:
        print(-1)
        continue

    if (d2-d1) % 6 != 0:
        print(-1)
        continue
    n = (d2 -d1) // 6
    d1 += 2 * n
    print(n + d1 // 2)
