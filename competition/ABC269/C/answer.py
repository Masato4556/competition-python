n = int(input())

digits = []

i = 0

while 1 << i <= n:
    if n & 1 << i > 0:
        digits.append(i)
    i += 1

d_len = len(digits)

results = []
for i in range(2 ** d_len):
    r = 0
    for j in range(d_len):
        if i & (1 << j):
            r += 2 ** digits[j-1]
    results.append(r)

results.sort()
for result in results:
    print(result)
