from math import log2, ceil
N = int(input())

M = ceil(log2(N))
print(M)

t = [list() for _ in range(M)]

# print(t)

for i in range(N):
    for j in range(M):
        if i >> j & 1:
            t[j].append(i+1)

for j in range(M):
    print(len(t[j]), *t[j])

S = list(map(int, input()))
# print(S)

ans = 0
for i in range(M):
    if S[i] == 0:
        continue
    ans += 2**i

print(ans+1)
