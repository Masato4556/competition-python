from fractions import Fraction

def clac_time(a, b, x):
    return Fraction(A) / Fraction(1+x)**Fraction('0.5') + B * x

A, B = map(int, input().split())

right = 0
left = A // B
cnt = 0
while True:
    mid = (right + left) // 2
    if left == right:
        break

    diff = clac_time(A, B, mid+1) - clac_time(A, B, mid)
    if diff > 0:
        left = mid
    elif diff < 0:
        right = mid + 1
    else:
        break
 
for i in range(1000):
    print(clac_time(A, B, mid+i))







