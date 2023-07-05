from collections import defaultdict
from itertools import combinations

S = input()


def f(s):
    n = len(s)
    cnts = [[0] * 10 for _ in range(n+1)]

    for i in range(n):
        for j in range(10):
            cnts[i+1][j] = cnts[i][j]
        si = int(s[i])
        cnts[i+1][si] += 1

    return cnts


def g(s, start, cnts):
    n = len(s)
    ok = set()
    for i in range(start+1, n+1):
        flag = 0
        for j in range(10):
            if (cnts[i][j] - cnts[start][j]) % 2 != 0: flag = 1
        if flag: continue
        ok.add(i)

    return ok

cnts = f(S)


ans = 0
for i in range(len(S)):
    ok = g(S, i, cnts)
    ans += len(ok)

print(ans)