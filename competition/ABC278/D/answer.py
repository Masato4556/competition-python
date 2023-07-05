from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

Q = int(input())

base = -1
i_adds = defaultdict(int)

for _ in range(Q):
    query = list(input().split())
    if query[0] == "1":
        x = int(query[1])
        base = x
        # base = int(query[1])
        i_adds = defaultdict(int)
    elif query[0] == "2":
        i = int(query[1]) - 1
        x = int(query[2])
        i_adds[i] += x
    else: 
        i = int(query[1]) - 1
        if base != -1:
            print(base + i_adds[i])
        else:
            print(A[i] + i_adds[i])
