
n = int(input())
s = [(c, -1) for c in input()]
q = int(input())

last_convert_query_i = -99
last_convert_query_t = -1

for i in range(q):
    t, x, c = input().split()
    x = int(x)-1
    if t == "1":
        s[x] = (c, i)
        continue

    last_convert_query_i = i
    last_convert_query_t = t

ans = []
for c, i in s:
    if i > last_convert_query_i:
        ans.append(c)
        continue
    ans.append(c.lower() if last_convert_query_t == "2" else c.upper())

print("".join(ans))
