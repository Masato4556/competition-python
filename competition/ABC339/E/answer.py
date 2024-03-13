import sys
from atcoder import segtree, lazysegtree
from atcoder.string import suffix_array
from bisect import bisect, bisect_left, insort, insort_left
from collections import deque, defaultdict, Counter
from copy import deepcopy
from functools import lru_cache
from heapq import heappush, heappop, heapify
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from math import ceil, floor, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, atan2, radians, degrees, log2, gcd
INF = float('inf')
sys.setrecursionlimit(10**9)
def f(x): return x
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(func): return map(func, input().split())
def LIST(func=f): return list(map(func,  input().split()))
def TUPLE(func=f): return tuple(map(func, input().split()))
def GRID(n): return [input() for _ in range(n)]
def ZIP(n, func=f): return zip(*(MAP(func) for _ in range(n)))


def segfunc(x, y):
    return max(x, y)


class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.leaf_num = 1 << (n-1).bit_length()
        self.tree = [ide_ele]*2*self.leaf_num  # インデックス0は利用せず、1以降のみを用いる

        # 葉ノードの初期化
        for i in range(n):
            self.tree[self.leaf_num+i] = init_val[i]
        # 葉ノード以外の初期化
        for i in range(self.leaf_num-1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])

    def add(self, ind, x):
        ind += self.leaf_num
        self.tree[ind] += x
        while ind > 1:
            self.tree[ind >> 1] = self.segfunc(
                self.tree[ind], self.tree[ind ^ 1])
            ind >>= 1

    def update(self, ind, x):
        ind += self.leaf_num
        self.tree[ind] = x
        while ind > 1:
            self.tree[ind >> 1] = self.segfunc(
                self.tree[ind], self.tree[ind ^ 1])
            ind >>= 1

    def query(self, left, right):
        # [left, right)の区間の計算結果を返す　
        # 全区間の計算結果を取得したいなら[0, N)
        # [i, i)の場合、区間が存在しないためide_eleを返す
        res = self.ide_ele
        left += self.leaf_num
        right += self.leaf_num
        while left < right:
            if left & 1:
                res = self.segfunc(res, self.tree[left])
                left += 1
            if right & 1:
                res = self.segfunc(res, self.tree[right-1])
            left >>= 1
            right >>= 1
        return res


N, D = MAP(int)
A = LIST(int)

segtree = segtree.SegTree(segfunc, 0, [0]*(5*10**5+1))

for a in A:
    prev = segtree.prod(max(1, a-D), min(5*10**5, a+D)+1)
    segtree.set(a, prev+1)

print(segtree.all_prod())
