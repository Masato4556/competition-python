from collections import deque, defaultdict
import heapq
from functools import lru_cache
import sys
sys.setrecursionlimit(10 ** 9)

N, M, D = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

i = N - 1
j = M - 1
while i >= 0 and j >= 0:
    if abs(A[i] - B[j]) <= D:
        print(A[i] + B[j])
        exit()

    if A[i] < B[j]:
        j -= 1
    else:
        i -= 1

print(-1)
