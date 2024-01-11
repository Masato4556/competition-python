from collections import deque


que = deque()
included = set()

S = input()

for c in S:
    if c == "(":
        que.append(c)
        included.add(c)
    elif c == ")":
        while len(que):
            v = que.pop()
            if v == "(":
                break
            included.remove(v)
    else:
        if c in included:
            print("No")
            exit()
        que.append(c)
        included.add(c)

print("Yes")
