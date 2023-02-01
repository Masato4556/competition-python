
from decimal import Decimal, ROUND_HALF_UP

x, k = map(int, input().split())

result = x
for i in range(k):
    result = int(Decimal(result).quantize(Decimal('1E{}'.format(i+1)), rounding=ROUND_HALF_UP))

print(result)