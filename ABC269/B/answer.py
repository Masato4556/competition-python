
a, b, c, d = 0, 0, 0, 0

S = [input() for _ in range(10)]

for i in range(10):
    for j in range(10):
        if S[i][j] == "#":
            a = i + 1
            c = j + 1
            break
    if a * c != 0:
        break

for i in range(10):
    for j in range(10):
        if S[9-i][9-j] == "#":
            b = 10-i
            d = 10-j
            break
    if b * d != 0:
        break

print(a, b)
print(c, d)