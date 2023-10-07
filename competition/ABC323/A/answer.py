s = input()

for i in range(1, 16, 2):
    if s[i] == "1":
        print("No")
        exit()
print("Yes")
