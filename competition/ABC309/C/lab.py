
import random


def solve(N, K, AB):
    AB.sort(reverse=True)

    cnt = 0
    prev_a = -1
    for i in range(N):
        a, b = AB[i]
        cnt += b
        if cnt > K and a != prev_a:
            print(a+1)
            return
        prev_a = a

    print(1)


N = 4
K = 0

AB = [
    [6, 3],
    [2, 5],
    [1, 9],
    [4, 2]
]
print(N, K, AB)
for i in range(20):
    solve(N, i, AB)
