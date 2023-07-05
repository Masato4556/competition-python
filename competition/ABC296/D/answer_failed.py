
N, M = map(int, input().split())

X = M
while X <= M**2:
    for i in range(1, N+1):
        if X % i == 0 and X // i <= N:
            print(X)
            exit()
    X += 1
print(-1)