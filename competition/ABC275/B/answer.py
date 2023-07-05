divisor = 998244353
a, b, c, d, e, f = map(int, input().split())
 
result = ((a * b * c) % divisor) - ((d * e * f) % divisor)
print(result + divisor if result < 0 else result)