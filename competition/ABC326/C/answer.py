from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

que = deque(A)
que2 = deque()
# print(que, que2)

while len(que) and que[0] < M:
    a = que.popleft()
    que2.append(a)

ans = len(que2)

# print(que, que2)

while len(que):
    a = que.popleft()
    que2.append(a)
    x = a + 1 - M
    while len(que2) and que2[0] < x:
        que2.popleft()
    # print(que, que2)
    if len(que2) > ans:
        ans = len(que2)

print(ans)