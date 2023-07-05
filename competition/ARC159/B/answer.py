def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


A, B = map(int, input().split())
A, B = max(A, B), min(A, B)

ans = 0
while A > 0 and B > 0:
    ans += 1
    g = gcd(A, B)
    A, B = A-g, B-g
    print(A, B)

print(ans)
