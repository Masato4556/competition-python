
N = int(input())
A = list(map(int, input().split()))
S = input()

CS_M = [[0 for _ in range(3)] for _ in range(N+1)]
CS_X = [[0 for _ in range(3)] for _ in range(N+1)]

inds_E = []

for i in range(N):
    for j in range(3):
        CS_M[i+1][j] = CS_M[i][j]
        CS_X[N-i-1][j] = CS_X[N-i][j]
    if S[i] == "M":
        CS_M[i+1][A[i]] += 1
    elif S[i] == "E":
        inds_E.append(i)
    if S[N-i-1] == "X":
        CS_X[N-i-1][A[N-i-1]] += 1

ans = 0

for i in inds_E:
    if A[i] == 0:
        ans += CS_M[i][0] * CS_X[i+1][0]
        ans += CS_M[i][0] * CS_X[i+1][1] * 2
        ans += CS_M[i][0] * CS_X[i+1][2]

        ans += CS_M[i][1] * CS_X[i+1][0] * 2
        ans += CS_M[i][1] * CS_X[i+1][1] * 2
        ans += CS_M[i][1] * CS_X[i+1][2] * 3

        ans += CS_M[i][2] * CS_X[i+1][0]
        ans += CS_M[i][2] * CS_X[i+1][1] * 3
        ans += CS_M[i][2] * CS_X[i+1][2]
    elif A[i] == 1:
        ans += CS_M[i][0] * CS_X[i+1][0] * 2
        ans += CS_M[i][0] * CS_X[i+1][1] * 2
        ans += CS_M[i][0] * CS_X[i+1][2] * 3

        ans += CS_M[i][1] * CS_X[i+1][0] * 2
        # ans += CS_M[i][1] * CS_X[i+1][1] * 0
        # ans += CS_M[i][1] * CS_X[i+1][2] * 0

        ans += CS_M[i][2] * CS_X[i+1][0] * 3
        # ans += CS_M[i][2] * CS_X[i+1][1] * 0
        # ans += CS_M[i][2] * CS_X[i+1][2] * 0
    else:
        ans += CS_M[i][0] * CS_X[i+1][0]
        ans += CS_M[i][0] * CS_X[i+1][1] * 3
        ans += CS_M[i][0] * CS_X[i+1][2]

        ans += CS_M[i][1] * CS_X[i+1][0] * 3
        # ans += CS_M[i][1] * CS_X[i+1][1] * 0
        # ans += CS_M[i][1] * CS_X[i+1][2] * 0

        ans += CS_M[i][2] * CS_X[i+1][0] * 1
        # ans += CS_M[i][2] * CS_X[i+1][1] * 0
        # ans += CS_M[i][2] * CS_X[i+1][2] * 0

print(ans)
