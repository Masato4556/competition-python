from copy import deepcopy
h, w = map(int, input().split())
A = []
for i in range(h):
    A.append(list(input()))

q = int(input())
query = []
for i in range(q):
    query.append(list(map(int, input().split())))


for a, b in query:
    A_temp = deepcopy(A)
    for i in range(a):
        for j in range(b):
            A_temp[i][j] = A[a-i-1][b-j-1]

    for i in range(a):
        for j in range(w-b):
            A_temp[i][j+b] = A[a-i-1][w-j-1]

    for i in range(h-a):
        for j in range(b):
            A_temp[i+a][j] = A[h-i-1][b-j-1]

    for i in range(h-a):
        for j in range(w-b):
            A_temp[i+a][j+b] = A[h-i-1][w-j-1]

    A = A_temp

for a_v in A:
    print("".join(a_v))
