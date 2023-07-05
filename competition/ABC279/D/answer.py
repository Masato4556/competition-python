from decimal import Decimal
from math import floor

def calc_time(a, b, x):
    return A/(x+1)**0.5 + B*x

A, B = map(int, input().split())

x = (A/(2*B))**(2/3)-1

ans = 10**18
for i in range(-10, 11):
    if x + 1 < 0: continue
    ans = min(ans, calc_time(A, B, floor(x+1)))

print(ans)







