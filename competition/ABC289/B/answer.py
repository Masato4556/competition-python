from collections import deque

n, m = map(int, input().split())
a = list(map(int, input().split()))

que = deque([])

for i in range(1, n+1):
    if i in a:
        que.append(i)
    else:
        print(i, end=" ")
        while len(que):
            v = que.pop()
            print(v, end=" ")
