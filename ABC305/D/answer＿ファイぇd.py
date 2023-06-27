# A のとりうる最大値が10**9なので、配列が巨大になりすぎて失敗する

N = int(input())
A = list(map(int, input().split()))

diff = [0] * (A[-1]+1)
S = [0] * (A[-1]+1)

for i in range(1, ((N-1) // 2) + 1):
    for j in range(A[2*i-1], A[2*i]):
        diff[j] += 1

for i in range(1, A[-1]+1):
    S[i] = S[i-1] + diff[i-1]

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())

    print(S[r] - S[l])
