# PyPy3 (7.3.0)	    2213 ms	225824 KB	TLE
# Python (3.8.2)	451 ms	10008 KB	AC
# Cython (0.29.16)	1916 ms	10308 KB	AC

n = int(input())
A = input()
B = input()

x = ""
y = ""
for i in range(n):
    if A[i] < B[i]:
        x += A[i]
        y += B[i]
    else:
        x += B[i]
        y += A[i]

x = int(x) % 998244353
y = int(y) % 998244353
print((int(x) * int(y)) % 998244353)
