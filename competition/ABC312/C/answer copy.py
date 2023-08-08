
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(lambda x: int(x)+1, input().split()))

A.sort()
B.sort()


a_i, b_i = 0, 0
a_cnt, b_cnt = 0, M

ans = 0
while a_i < N and b_i < M:
    print("A, B:", A[a_i], B[b_i])
    if A[a_i] < B[b_i]:
        ans = A[a_i]
        a_cnt += 1
        a_i += 1
    elif A[a_i] > B[b_i]:
        ans = B[b_i]
        b_cnt -= 1
        b_i += 1
    else:
        ans = A[a_i]
        a_cnt += 1
        a_i += 1
        b_cnt -= 1
        b_i += 1
    print(a_i, b_i, a_cnt, b_cnt)

    if a_cnt >= b_cnt:
        break

print(ans)
