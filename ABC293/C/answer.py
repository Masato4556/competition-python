from itertools import combinations
h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]

ans = 0
for rt in combinations(range(w + h - 2), w-1):
    prevs = set()
    prevs.add(A[0][0])
    r, c = 0, 0
    for i in range(w + h - 2):
        if i in rt:
            c += 1
        else:
            r += 1
        if A[r][c] in prevs:

            break
        prevs.add(A[r][c])
    if len(prevs) == h + w  -1:
        ans +=1

print(ans)