
Q = int(input())

arr = []
for _ in range(Q):
    a, b = map(int, input().split())
    if a == 1:
        arr.append(b)
    else:
        print(arr[-b])
