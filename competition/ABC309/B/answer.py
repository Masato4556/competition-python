
N = int(input())

S = [input() for _ in range(N)]

for i in range(N):
    row = []
    if i == 0:
        row.append(S[1][0])
        for j in range(1, N):
            row.append(S[0][j-1])
    elif i == N-1:
        for j in range(N-1):
            row.append(S[-1][j+1])
        row.append(S[-2][-1])
    else:
        row.append(S[i+1][0])
        for j in range(1, N-1):
            row.append(S[i][j])
        row.append(S[i-1][-1])
    print("".join(row))
