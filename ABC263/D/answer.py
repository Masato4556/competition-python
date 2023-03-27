# testcase 6　で落ちてしまう

def f(arr):
    n = len(arr)
    res = [0] * (n+1)
    for i in range(1, n+1):
        res[i] = res[i-1] + arr[i-1]
    return res


N, L, R = map(int, input().split())
A = list(map(int, input().split()))

if L > R:
    L, R = R, L
    A.reverse()

S = f(A)
A.reverse()
S_rev = f(A)


ll = [0]
rr = [0]

m = 0
prev = -1
for i in range(1, N+1):
    if L*i - S[i] < m:
        m = L*i - S[i]
        prev = i
    else:
        if prev == -1: continue 
        ll.append(i-1)
        prev = -1
if prev != -1: 
    ll.append(i)


m = 0
prev = -1
for i in range(1, N+1):
    if R*i - S_rev[i] < m:
        m = R*i - S_rev[i]
        prev = i
    else:
        if prev == -1: continue 
        rr.append(i-1)
        prev = -1
if prev != -1: 
    rr.append(i)


ans = sum(A)
rr.reverse()
for l in ll:
    for r in rr:
        if l > (N-r): continue
        ans = min(ans, S_rev[-1] - S_rev[r] - S[l] + r*R + l*L)
        break

print(ans)