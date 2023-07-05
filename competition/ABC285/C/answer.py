
a_ord = ord('A')

s = input()[::-1]

result = 0
for i, c in enumerate(s):
    result += (ord(c) - a_ord + 1) * (26 ** i)
print(result)