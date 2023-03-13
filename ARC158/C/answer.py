from functools import lru_cache
@lru_cache(None)
def f(n):
    s = str(n)

    array = list(map(int, s))
    return sum(array)

n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(n):
        ans += f(a[i] + a[j])

print(ans)