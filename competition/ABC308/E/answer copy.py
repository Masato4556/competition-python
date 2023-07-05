
N = int(input())
A = list(map(int, input().split()))
S = input()

conv = {
    "M": 0,
    "E": 1,
    "X": 2
}

B = [[0] * 3 for _ in range(3)]

for i in range(N):
    B[conv[S[i]]][A[i]] += 1

ans = 0

ans += B[0][0] * B[1][0] * B[2][0]

ans += B[0][1] * B[1][0] * B[2][0] * 2
ans += B[0][0] * B[1][1] * B[2][0] * 2
ans += B[0][0] * B[1][0] * B[2][1] * 2
ans += B[0][0] * B[1][1] * B[2][1] * 2
ans += B[0][1] * B[1][0] * B[2][1] * 2
ans += B[0][1] * B[1][1] * B[2][0] * 2

ans += B[0][0] * B[1][1] * B[2][2] * 3
ans += B[0][0] * B[1][2] * B[2][1] * 3
ans += B[0][1] * B[1][0] * B[2][2] * 3
ans += B[0][1] * B[1][2] * B[2][0] * 3
ans += B[0][2] * B[1][0] * B[2][1] * 3
ans += B[0][2] * B[1][1] * B[2][0] * 3

print(ans)
