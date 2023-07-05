

n, s = map(int, input().split())
cards = [tuple(map(int, input().split())) for _ in range(n)]

result = [["" for _ in range(s+1)] for _ in range(n)]

for i in range(n):
    if i == 0:
        if cards[i][0] <= s:
            result[i][cards[i][0]] = "H"
        if cards[i][1] <= s:
            result[i][cards[i][1]] = "T"

    for j, prev in enumerate(result[i-1]):
        if not prev: continue
        if j + cards[i][0] <= s:
            result[i][j + cards[i][0]] = prev + "H"
        if j + cards[i][1] <= s:
            result[i][j + cards[i][1]] = prev + "T"

if result[-1][-1] == "":
    print("No")
else:
    print("Yes")
    print(result[-1][-1])
