from itertools import combinations

n, m = map(int, input().split())
S = [input() for _ in range(n)]

ans = 0
for ss in combinations(S, 2):
    flag = True
    for c1, c2 in zip(ss[0], ss[1]):
        if c1 == "o" or c2 == "o": continue
        flag = False

    if flag:
        ans += 1

print(ans)