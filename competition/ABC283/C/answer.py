s = input()

length = len(s)
result = length
next_skip = False
for i in range(length-1):
    if next_skip: 
        next_skip = False
        continue
    if s[i] == "0" and s[i+1] == "0":
        result -= 1
        next_skip = True
print(result)