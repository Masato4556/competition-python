from collections import defaultdict

def isValid(x, n, count):
    sx = str(x)
    xcount = defaultdict(int)

    for s in str(x).zfill(n):
        xcount[s] += 1

    for i in range(0,10):
        stri = str(i)
        if count[stri] != xcount[stri]:
            return 0
    return 1

def solve():
    N = int(input())
    S = input()
    count = defaultdict(int)
    for s in S:
        count[s] += 1

    ans = 0
    for i in range(3162278):
        if isValid(i**2, N, count):
            ans += 1

    print(ans)

solve()