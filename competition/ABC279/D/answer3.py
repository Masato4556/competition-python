from fractions import Fraction
from decimal import Decimal

def f(a, b, x):
    return Decimal(-0.5) * Decimal(A) * Decimal(1+x)**Decimal('-1.5') + Decimal(B)
def calc_time(a, b, x):
    return Decimal(A) * Decimal(1+x)**Decimal('-0.5') + Decimal(B) * Decimal(x) 

A, B = map(int, input().split())

left = 0
right = A // B
cnt = 0
while True:
    mid = (right + left) // 2
    if left == right:
        break

    d = f(A, B, mid+1)
    if d > 0:
        right = mid -1
    elif d < 0:
        left = mid + 1
    else:
        print("nbnn")
        break

print(min(calc_time(A, B, mid), calc_time(A, B, mid+1)))







