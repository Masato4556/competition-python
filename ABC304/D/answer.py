from collections import defaultdict


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


W, H = map(int, input().split())
N = int(input())
PQ = [list(map(int, input().split())) for _ in range(N)]

A = []
B = []
A_N = int(input())
A .extend(list(map(int, input().split())))
B_N = int(input())
B.extend(list(map(int, input().split())))

cnt = defaultdict(int)
for p, q in PQ:
    a_i = binary_search(A, p)
    b_i = binary_search(B, q)
    cnt[(a_i, b_i)] += 1

c = [v for v in cnt.values()]

print(0 if len(c) < (A_N+1)*(B_N+1)
      else min(c), max(c))
