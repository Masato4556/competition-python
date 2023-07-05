

N, X = map(int, input().split())
A = set(map(int, input().split()))

for a in A:
    if (a - X) in A:
        print("Yes")
        exit()

print("No")