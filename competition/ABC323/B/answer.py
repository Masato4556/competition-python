n = int(input())

s = [input() for _ in range(n)]

win_num = [0] * n
for i in range(n):
    for j in range(n):
        if s[i][j] == "o":
            win_num[i] += 1


rank = list(sorted(enumerate(win_num), key=lambda x: x[1], reverse=True))

ans = []
for r in rank:
    ans.append(r[0]+1)

print(*ans)
