n, m = map(int, input().split())
S = []
for _ in range(m):
    input()
    S.append(set(map(int, input().split())))

result = 0
for i in range(2**m):
    r = set()
    for ind, s in enumerate(S):
        if i & (1 << ind):
            r |= s
    if len(r) == n:
        result += 1

print(result)
