# testcase 6　で落ちてしまう

def f(arr):
    n = len(arr)
    res = [0] * (n+1)
    for i in range(1, n+1):
        res[i] = res[i-1] + arr[i-1]
    return res


N, L, R = map(int, input().split())
A = list(map(int, input().split()))

S = f(A)

l_cnt = 0
r_cnt = 0

m = 0
for i in range(1, N+1):
    if L*i - S[i] < m:
        m = L*i - S[i]
        l_cnt = i

for i in range(l_cnt):
    A[i] = L

S_rev = f(A[::-1])

m = 0
for i in range(1, N+1):
    if R*i - S_rev[i] < m:
        m = R*i - S_rev[i]
        r_cnt = i

print(S_rev[-1] - S_rev[r_cnt] + r_cnt*R)
