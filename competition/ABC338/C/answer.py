
N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# print(Q)
# print(A)
# print(B)

min_a_count = 10**10
for i in range(N):
    if A[i] == 0:
        continue
    min_a_count = min(min_a_count, Q[i] // A[i])

# print(min_a_count)

max_a = max(A)

ans = 0
for k in range(min_a_count+1):
    min_m = 10**10
    for n in range(N):
        if Q[n] - k * A[n] < 0:
            min_m = -1
            break
        if B[n] == 0:
            continue
        m = (Q[n] - k * A[n]) // B[n]
        # print(Q[n], k*A[n], B[n], m)
        min_m = min(min_m, m)
    if min_m >= 0:
        # print(k, min_m)
        ans = max(ans, k+min_m)

print(ans)
