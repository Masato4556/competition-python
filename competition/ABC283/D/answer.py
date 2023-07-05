def f(s, i):
    v = 0
    for j in range(i, -1, -1):
        s_j = s[j]
        if s_j == "(": v += 1
        if s_j == ")": v -= 1

        if v > 0: 
            return j+1
    return 0

s = input()
len_s = len(s)
box = [""] * len_s

result = "Yes"
for i in range(len_s):
    s_i = s[i]
    if s_i == "(": continue
    if s_i == ")": 
        j = f(s, i)
        for k in range(j, i):
            box[k] = ""
        continue
    if s_i in box:
        result = "No"
        break
    box[i] = s_i

print(result)
print(box)
