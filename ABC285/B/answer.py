
n = int(input())
s = input()

for i in range(1, n):
    count = 0
    for j in range(n-i):
        # print(s[j], s[j+i], j, j+1)
        if s[j] == s[j+i]:
            break
        count += 1
    print(count)
