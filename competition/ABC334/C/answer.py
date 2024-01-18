
N, K = map(int, input().split())
A = list(map(int, input().split()))

if K == 1:
    print(0)
    exit()

A.sort()

s_l = [0]
s_r = [0]
for i in range(K//2):
    s_l.append(A[2*i+1]-A[2*i] + s_l[-1])
    s_r.append(A[K-2*i-1]-A[K-(2*i+1)-1] + s_r[-1])

# print(A)
# print(s_l)
# print(s_r)

print(min([s_l[i] + s_r[K//2 - i] for i in range(K//2+1)]))
