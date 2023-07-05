N = int(input())
A = list(map(int, input().split()))

Q = int(input())

i_adds = [0] * N
reset = False
base = 0
for _ in range(Q):
    query = list(input().split())
    
    if query[0] == "1":
        x = int(query[1])
        reset = True
        base = x
        i_adds = [0] * N
    elif query[0] == "2":
        i = int(query[1]) - 1
        x = int(query[2])
        i_adds[i] += x
    else: 
        i = int(query[1]) - 1
        if reset:
            print(base + i_adds[i])
        else:
            print(A[i] + i_adds[i])