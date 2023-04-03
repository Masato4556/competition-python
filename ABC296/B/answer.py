def get_alphabet(i):
    return chr(ord('a') + i - 1)

for i in range(8):
    S = input()
    if "*" in S:
        print(get_alphabet(S.index("*")+1) + str(8-i))
