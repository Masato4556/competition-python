
S = input()
N = int(input())

base = 0
ss = []
S = S[::-1]
for i in range(len(S)):
    if S[i] == "?":
        ss.append(i)
    elif S[i] == "1":
        base += 2 ** i

ss.reverse()

if base > N:
    print(-1)
    exit()

ans = base
for j in range(len(ss)):
    if ans + 2**ss[j] <= N:
        ans += 2**ss[j]

print(ans)
