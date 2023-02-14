n, k = map(int, input().split())
A = list(map(int, input().split()))

result = 0
t = True
for i in range(k):
    a = A[k - 1 - i]
    q, r = divmod(n, a)
    n = r
    if q % 2 == 0:
        result += a * (q // 2)
    else:
        if t:
            result += a * (q // 2 + 1) 
        else:
            result += a * (q // 2)
        t = not t

print(result)
