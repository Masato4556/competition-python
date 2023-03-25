from collections import defaultdict
from itertools import permutations

n, m = map(int, input().split())
S = []
sum_S_len = 0
X_min, X_max = 3, 16
for _ in range(n):
    S.append(input())
    sum_S_len += len(S[-1])

# TODO キャッシュ
def f(s):
    if s in S:
        return S.index(s)
    return -1

# TODO おける_の数を考える

T = defaultdict(set)
for _ in range(n):
    t = input()

    i = 0
    flg = 1
    h = []
    separator_nums = []
    for j in range(len(t)):
        if flg == 1 and t[j] == "_":
            a = f(t[i:j])
            if a == -1: break
            h.append(a)
            i = j
            flg *= -1

        if flg == -1 and t[j] != "_":
            separator_nums.append(j-i)
            i = j
            flg *= -1

        j += 1

    a = f(t[i:])
    if a != -1:
        h.append(a)

    if len(h) != n: break

    T[tuple(h)].add(tuple(separator_nums))


print(T)
print(sum_S_len)
sep_min, sep_max = max(0, X_min - sum_S_len), min(0, X_max - sum_S_len)
print(sep_min, sep_max)
print()

for p in permutations(range(n)):
    print(p, T[p])