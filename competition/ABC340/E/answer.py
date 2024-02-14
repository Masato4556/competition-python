from atcoder.lazysegtree import LazySegTree
import sys
INF = float('inf')
sys.setrecursionlimit(10**9)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int,  input().split()))
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))


n, m = MAP()
A = LIST()
B = LIST()

seg = LazySegTree(op=min, e=INF, mapping=lambda f, x: f+x,
                  composition=lambda f, g: f+g, id_=0, v=A)

for b in B:
    x = seg.get(b)
    seg.apply(b, f=-x)
    q, m = divmod(x, n)
    if q > 0:
        seg.apply(0, n, q)
    if m > 0:
        if b + m < n:
            seg.apply(b+1, b+1+m, 1)
        else:
            seg.apply(b+1, n, 1)
            seg.apply(0, m-(n-b-1), 1)

print(*[seg.get(i) for i in range(n)])
