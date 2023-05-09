
from functools import lru_cache
import sys

sys.setrecursionlimit(10**6)


N = int(input())
A = list(map(int, input().split()))
cnt = 0


@lru_cache(None)
def f(s, e):
    if s == e:
        return A[s]
    return max(A[s] - f(s+1, e), A[e] - f(s, e-1))


print(f(0, N-1))
