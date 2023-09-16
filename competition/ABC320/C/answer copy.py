from collections import defaultdict
M = int(input())
S = [input() for _ in range(3)]

c = defaultdict(int)

for i in range(M):
    for j in range(3):
        c[int(S[j][i])] |= 1 << j
    # print(c)
    for k in range(10):
        print(i, k, c[k])
        if c[k] == 7:
            print(i+1)
            exit()

print(-1)
