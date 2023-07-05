
N = int(input())
S = [input() for _ in range(N)]
S_set = set(S)

if len(S) != len(S_set):
    print("No")
    exit()

first_validation = ("H", "D", "C", "S")
second_validation = ("A" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "T" , "J" , "Q" , "K")
for s in S:
    if s[0] in first_validation and s[1] in second_validation: continue

    print("No")
    exit()

print("Yes")

