
S = input()

if len(S) == 1:
    print("Yes" if S.isupper() else "No")
    exit()

if S[0].isupper() and S[1::].islower():
    print("Yes")
else:
    print("No")
