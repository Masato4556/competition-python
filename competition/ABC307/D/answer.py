from collections import deque

N = int(input())
S = input().strip()

que = deque()
ans = ""

for c in S:
    if c == "(":
        que.append([c])
        continue

    if len(que) == 0:
        ans += c
        continue

    if c == ")":
        que.pop()
        continue

    que[-1].append(c)

while len(que):
    ans += "".join(que.popleft())

print(ans)
