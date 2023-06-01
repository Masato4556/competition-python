N = int(input())
S = input()
T = input()


for s, t in zip(S, T):
    if s == t:
        continue
    if s in ("l", "1") and t in ("l", "1"):
        continue
    if s in ("0", "o") and t in ("0", "o"):
        continue
    print("No")
    exit()


print("Yes")
