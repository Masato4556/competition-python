
def nand(x, y):
    return int(not x or not y)


def cumulative_sum(array):
    n = len(array)
    cumsum = [0] * (n+1)
    for i in range(n):
        cumsum[i+1] = cumsum[i] + array[i]
    return cumsum


N = int(input())
S = [int(s) for s in input()]

A = []

a = S[0]
A.append(S[0])
for i in range(1, N):
    a = nand(a, S[i])
    A.append(a)

SA = cumulative_sum(A)

ans = 0
for i in range(N):
    if S[i] == 0:
        ans += SA[N-i] - SA[1]
        print(i, N-1)
    else:
        ans += N-i - SA[N-i] + SA[1]
        print(N-1, i+1)

print(A)
print(SA)
print(ans)
