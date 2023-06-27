# Python3
import numpy as np

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

a = np.array(A)
b = np.array(B)

for i in range(4):
    if np.min(b - a) >= 0:
        print("Yes")
        exit(0)

    a = np.rot90(a)

print("No")
