from collections import defaultdict
n = int(input())

cards = []
counter = defaultdict(int)
for _ in range(n):
    a, b = map(int, input().split())
    cards.append([a, b])
    counter[a] += 1
    counter[b] += 1

r = 0
for i in range(2 ** n):
    prev = -1
    for j in range(n):
        if (1 << j) & i:
            curr = cards[j][0]
        else:
            curr = cards[j][1]

        if curr == prev:
            r += 1
            break
        prev = curr

print(((2 ** n) - r) % 998244353)