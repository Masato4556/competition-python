from collections import defaultdict
from scipy.special import comb
from functools import lru_cache

@lru_cache(None)
def f(x):
    return int(comb(x, 2)) + int(comb(x, 3))

N = int(input())
A = list(map(int, input().split()))

g = defaultdict(list)

# iをAiの値でグルーピング
for i in range(N):
    g[A[i]].append(i)

ans = 0
for inds in g.values():
    index_num = len(inds)
    if index_num < 2:
        continue

    # sum(k-i-1 {Ai = Ak = x かつ i != k}) - kC3 {k=(Ai=xとなるiの個数)}
    for i in range(index_num-1):
        ans += (inds[i+1] - inds[i]) * ((i+1) * (index_num-1-i))
    ans -= f(index_num)

print(ans)