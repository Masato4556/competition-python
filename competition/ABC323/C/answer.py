

N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]

# print(A)
# print(S)

points = [i+1 for i in range(N)]

# print(points)

for i in range(N):
    for j in range(M):
        if S[i][j] == "o":
            points[i] += A[j]

# print(points)

max_point = max(points)

# print(max_point, max_point_ind)

sorted_A = sorted(enumerate(A), key=lambda x: x[1], reverse=True)

ans = [0] * N
for i in range(N):
    if points[i] == max_point:
        continue
    for a in sorted_A:
        if points[i] > max_point:
            break
        if S[i][a[0]] == 'o':
            continue
        points[i] += a[1]
        ans[i] += 1


for row in ans:
    print(row)
