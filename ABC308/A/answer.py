
S = list(map(int, input().split()))

prev = -1
for s in S:

    if not (100 <= s <= 675) or s % 25 != 0 or s < prev:
        print("No")
        exit()
    prev = s

print("Yes")
