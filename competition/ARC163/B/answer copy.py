
N, M = map(int, input().split())
A_temp = list(map(int, input().split()))

left = A_temp[0]
right = A_temp[1]
A = A_temp[2:]

A.sort()
# print(left, right, A)
len_A = len(A)

ans = 10**12
for i in range(len_A-M+1):

    min_left = A[i-1]+1 if i-1 >= 0 else 0
    max_left = A[i]

    min_right = A[i+M-1]
    max_right = A[i+M]-1 if i+M < len_A else 10**9+1
    # print(i, f"left: {min_left}-{max_left}, rigth: {min_right}-{max_right}")

    ans_i = 0

    if left < min_left:
        ans_i += min_left - left
    elif left > max_left:
        ans_i += left - max_left
    # print(ans_i)

    if right < min_right:
        ans_i += min_right - right
    elif right > max_right:
        ans_i += right - max_right
    # print(ans_i)

    ans = min(ans, ans_i)

print(ans)
