x, y, n = map(int, input().split())
print(min(x * n, (n // 3) * y + (n % 3) * x ))
