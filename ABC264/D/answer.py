from collections import deque
s = input()
target = "atcoder"

que = deque(s)
que2 = deque([])

i = 0
ans = 0
while len(que):
    v = que.popleft()
    if v == target[i]:
        i += 1
        ans += len(que2)
    else:
        que2.append(v)

    if not len(que):
        que = que2
        que2 = deque([])

print(ans)
