s = input()

ans = ""
for i in range(len(s)):
    if i % 2 == 0: continue
    ans += s[i] + s[i-1]

print(ans)