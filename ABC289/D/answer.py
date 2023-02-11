from collections import deque

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
x = int(input())

result = [0 for _ in range(x+1)]

for b in B:
    result[b] = -1

que = deque([0])

fin = False
while len(que):
    v = que.pop()
    for a in A:
        if v+a > x: continue
        if result[v+a] == -1: continue
        if result[v+a] == 1: continue

        result[v+a] = 1
        que.append(v+a)

print("Yes" if result[-1] == 1 else "No")
