import sys
from atcoder import lazysegtree
from atcoder.string import suffix_array
from bisect import bisect, bisect_left, insort, insort_left
from collections import deque, defaultdict, Counter
from copy import deepcopy
from functools import lru_cache
from heapq import heappush, heappop, heapify
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from math import ceil, floor, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, atan2, radians, degrees, log2, gcd, perm, comb
INF = float('inf')
sys.setrecursionlimit(10**9)
def f(x): return x
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(func=f): return map(func, input().split())
def LIST(func=f): return list(map(func, input().split()))
def TUPLE(func=f): return tuple(map(func, input().split()))
def GRID(n): return [input() for _ in range(n)]
def ZIP(n, func=f): return zip(*(MAP(func) for _ in range(n)))


'''
辞書最小になるように先頭から部分列の文字を選択していく

まず、部分列先頭の文字は、後ろにK-1文字必要になるため i < N-K の範囲で選ばれる。
i < N-K の範囲の中で、最も辞書最小の文字を選ぶ。（もし範囲内に辞書最小の文字が複数ある場合は、インデックスが小さい方を選ぶ）

2文字目は、(1文字目のインデックス) < i < N-K+1 の範囲で辞書最小の文字を選ぶ。（もし範囲内に辞書最小の文字が複数ある場合は、インデックスが小さい方を選ぶ）
3文字目は、(2文字目のインデックス) < i < N-K+2 の範囲で辞書最小の文字を選ぶ。（もし範囲内に辞書最小の文字が複数ある場合は、インデックスが小さい方を選ぶ）
  :
K文字目は、(K-1文字目のインデックス) < i < N の範囲で辞書最小の文字を選ぶ。（もし範囲内に辞書最小の文字が複数ある場合は、インデックスが小さい方を選ぶ）
'''

N, K = MAP(int)
S = input()

heap = []
next = 0
ans = []
for i in range(N):
    heappush(heap, (S[i], i))
    if N > i + K:
        continue

    while True:
        s, j = heappop(heap)
        if next <= j:
            next = j + 1
            ans.append(s)
            break

print("".join(ans))
