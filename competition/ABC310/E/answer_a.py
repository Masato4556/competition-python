from functools import lru_cache

N = int(input())
S = [int(s) for s in input()]


@lru_cache(None)
def f(i, j):
    if i == j:
        return int(S[i])
    if S[j] == 0 or f(i, j-1) == 0:
        return 1

    return 0


ans = 0
for i in range(N):
    for j in range(i, N):
        ans += f(i, j)
print(ans)
