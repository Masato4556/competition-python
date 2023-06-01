from collections import deque, defaultdict
import heapq
from functools import lru_cache
import sys
sys.setrecursionlimit(10 ** 9)


X, Y, Z = map(int, input().split())
S = input()
N = len(S)
A = []

ans = 0
A_start = 0
for i in range(N):
    if S[i] == "A":
        A_start = i
        break
    ans += X

dp
for i in range(A_start, N):
