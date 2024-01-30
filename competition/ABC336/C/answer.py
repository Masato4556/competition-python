def MtoN(m, n, num):
    s = 0
    i = 0
    while num > 0:
        r = num % n
        s = s+r*m**i
        num = num//n
        i = i+1
    return s


N = int(input())
print(MtoN(10, 5, N-1) * 2)
