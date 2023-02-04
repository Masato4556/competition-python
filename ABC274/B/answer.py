h, w = map(int, input().split())
result = [0] * w
for _ in range(h):
    c = input()
    for j in range(w):
        if c[j] == "#":
            result[j] += 1

print(*result)
