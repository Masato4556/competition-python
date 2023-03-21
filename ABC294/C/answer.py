from collections import deque
N, M = map(int, input().split())
A = deque(list(map(int, input().split())))
B = deque(list(map(int, input().split())))

A_inds = []
B_inds = []
for i in range(1, N+M+1):
    if len(A) > 0 and len(B) > 0:
        if A[0] < B[0]:
            A_inds.append(i)
            A.popleft()
        else:
            B_inds.append(i)
            B.popleft()
    else:
        if len(A):
            A_inds.append(i)
            A.popleft()
        else:
            B_inds.append(i)
            B.popleft()

print(*A_inds)
print(*B_inds)
