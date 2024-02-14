from math import floor, ceil
from functools import lru_cache


N = int(input())


@lru_cache(None)
# def f(x):
#     if x <= 1:
#         return 0
#     return x + f(floor(x/2)) + f(ceil(x/2))
def f(x):
    if x <= 1:
        return 0
    return x + f(x//2) + f((x+1)//2)


print(f(N))
