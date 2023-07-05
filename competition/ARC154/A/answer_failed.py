n = int(input())
A = input()
B = input()

x, y = 0, 0
for i in range(n):
    a_i = int(A[i])
    b_i = int(B[i])
    if a_i < b_i:
        x += a_i * 10 ** (n-i-1)
        y += b_i * 10 ** (n-i-1)
    else:
        x += b_i * 10 ** (n-i-1)
        y += a_i * 10 ** (n-i-1)   

    x %= 998244353
    y %= 998244353 

print((x * y) % 998244353)
