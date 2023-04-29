
N = int(input())
S = input()

if "-" not in S or "o" not in S:
    print(-1)
    exit()

ans = -1
for s in S.split("-"):
    if len(s) > 0:
        ans = max(ans, len(s))

print(ans)
