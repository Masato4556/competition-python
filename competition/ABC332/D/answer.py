from itertools import permutations


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

ans = float('inf')
for row_inds in permutations(range(H)):
    for col_inds in permutations(range(W)):
        is_valid = True
        for a_h, b_h in enumerate(row_inds):
            for a_w, b_w in enumerate(col_inds):
                is_valid &= A[a_h][a_w] == B[b_h][b_w]
        if is_valid:
            ans = min(ans, min_swaps(list(row_inds)) +
                      min_swaps(list(col_inds)))

print(-1 if ans == float('inf') else ans)
