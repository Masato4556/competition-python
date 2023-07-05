
S = input()

Number = {str(i) for i in range(10)}

if len(S) != 8:
    print("No")
    exit()

if S[0] in Number or S[-1] in Number:
    print("No")
    exit()

for i in range(1, 7):
    if S[i] not in Number:
        print("No")
        exit()

print("Yes" if int(S[1:-1]) >= 100000 else "No")