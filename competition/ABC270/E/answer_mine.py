n, k = map(int, input().split())
A = list(map(int, input().split()))

# 最小値から取り出したいが、配列Aの順番を並び替えたくないので、
# このようにAのインデックスだけを並び替えるようにしている
A_ind = [*range(n)]
A_ind.sort(key=lambda i: A[i])

loop = 0
not_zero_len = n
prev_A_min = 0
for i in range(n):
    a = A[A_ind[i]] - prev_A_min
    if k < (a) * not_zero_len: 
        break
    
    k -= (a) * not_zero_len
    loop += a
    not_zero_len -= 1
    prev_A_min = A[A_ind[i]]

if not_zero_len == 0:
    print(*[0]*n)
    exit()

loop += k // (not_zero_len)
k %= not_zero_len

for i in range(n):
    A[i] = max(0, A[i] - loop)
    if A[i] > 0 and k > 0:
        A[i] -= 1
        k -= 1

print(*A)
