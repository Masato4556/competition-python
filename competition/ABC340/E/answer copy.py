
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# print(A)
# print(B)
# diff = []

for i in B:
    div = A[i] // N
    mod = A[i] % N
    # print(div, mod)

    for j in range(N):
        if j == 0:
            A[(i+j) % N] = div
        elif j <= mod:
            A[(i+j) % N] += div+1
        else:
            A[(i+j) % N] += div
    # print(A)

print(*A)
