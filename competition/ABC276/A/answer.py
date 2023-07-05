
s = input()
result = -1
for i in range(len(s)-1, -1, -1):
    if s[i] == "a":
        result = i+1
        break

print(result)

