from itertools import permutations


def transpose(A):
    return list(zip(*A))


def gen_swap_inds(A, B):
    inds_list = []
    for p in permutations(list(range(len(A)))):
        is_valid = True
        for i, j in enumerate(p):
            if len(set(A[i]) ^ set(B[j])) != 0:
                is_valid = False
                break

        if is_valid:
            inds_list.append(list(p))

    if len(inds_list) > 0:
        return inds_list

    print(-1)
    exit()


def min_swaps(arr):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_count += 1

    return swap_count


H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

row_inds_list = gen_swap_inds(A, B)

A = transpose(A)
B = transpose(B)

col_inds_list = gen_swap_inds(A, B)

min_row_swap_count = float('inf')
for row_inds in row_inds_list:
    min_row_swap_count = min(min_row_swap_count, min_swaps(row_inds))

min_col_swap_count = float('inf')
for col_inds in col_inds_list:
    min_col_swap_count = min(min_col_swap_count, min_swaps(col_inds))
print(min_row_swap_count + min_col_swap_count)
