from math import factorial
from collections import defaultdict

S = input()
n = len(S)
B = [0] * (n + 1)

D = defaultdict(int)
D[0] += 1

for i in range(n):
    B[i+1] = B[i] ^ (1 << int(S[i]))
    D[B[i+1]] += 1

ans = 0

for v in D.values():
    if v == 1: continue
    ans += factorial(v) // (factorial(v-2) * factorial(2))

print(ans)