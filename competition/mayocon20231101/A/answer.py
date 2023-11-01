from collections import deque
N, M = map(int, input().split())
A = list(map(lambda x: int(x)-1, input().split()))
A.sort(reverse=True)

que = deque(A)

ans = [0] * N

cnt = 0
for i in range(N-1, -1, -1):
    cnt += 1
    if len(que) and i == que[0]:
        que.popleft()
        cnt = 0
    ans[i] = cnt

for i in range(N):
    print(ans[i])
