
A, X, M = map(int, input().split())

if A == 1:
    print(X % M)
    exit()

print( (pow(A, X, M*(A-1))-1) // (A-1) % M )
