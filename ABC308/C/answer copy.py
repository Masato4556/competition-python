from decimal import Decimal
N = int(input())

ans = []
for i in range(N):
    a, b = map(Decimal, input().split())

    ans.append((a/(a+b), -1 * (i+1)))

ans.sort(reverse=True)
print(*[a[1] * -1 for a in ans])
