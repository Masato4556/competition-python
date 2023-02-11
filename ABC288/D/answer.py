N, K = map(int, input().split())
A = list(map(int, input().split()))
Q = int(input())

for _ in range(Q):
    l, r = map(lambda x: int(x)-1, input().split())
    X = A[l:r+1]
    n = len(X)
    for i in range(n-K, -1, -1):
        c = X[i+K-1]
        X2 = [x - c for x in X[i:i+K]]
        X = X[0:i]
        X.extend(X2)
    print("Yes" if all([x == 0 for x in X]) else "No")


