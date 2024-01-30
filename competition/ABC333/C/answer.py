from itertools import combinations_with_replacement

N = int(input())

a = list(map(lambda x: sorted(x, reverse=True),
         combinations_with_replacement(range(1, 13), 3)))
a.sort()
ans = 0
for i in range(3):
    ans += sum([10**i for i in range(a[N-1][i])])
print(ans)
