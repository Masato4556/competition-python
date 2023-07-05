# テストデータ生成など、回答とは関係のないコードを実行するファイル
from itertools import permutations
from collections import defaultdict
from random import shuffle
import bisect

def calc_lis_len(seq):
    lis = [seq[0]]
    for i in range(len(seq)):
        if seq[i] > lis[-1]:
            lis.append(seq[i])
        else:
            lis[bisect.bisect_left(lis, seq[i])] = seq[i]

    return len(lis)

def f(inds, a, b):
    pa = [a[i] for i in inds]
    pb = [b[i] for i in inds]
    a_lis_len = calc_lis_len(pa)
    b_lis_len = calc_lis_len(pb)
    return (a_lis_len + b_lis_len, pa, pb)

N = 7

A = list(range(1, N+1))
B = list(range(1, N+1))
shuffle(A)
shuffle(B)

print(A, B)

print("======")
max_lis_len = 0
for i in range(1, N+1):
    print("======", i)
    for inds in permutations(range(i)):
        lis_len, pa, pb, = f(inds, A, B)
        if lis_len >= max_lis_len:
            max_lis_len = lis_len
            print(lis_len, pa, pb)
