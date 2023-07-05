from itertools import combinations

def f(xi, xj, xk):
    return (xi + xj + xk) / (xi * xj * xk)

n = int(input())
x = list(map(int, input().split()))

x_plus = [v for v in x if v > 0]
x_minus = [v for v in x if v < 0]
x_plus.sort()
x_minus.sort()

if len(x_plus) > 6:
    x_plus = x_plus[:3] + x_plus[-4:]
if len(x_minus) > 6:
    x_minus = x_minus[:3] + x_minus[-4:]

xx = x_plus + x_minus
ans_min = 10000
ans_max = -10000

for xs in combinations(xx, 3):
    ans_min = min(ans_min, f(xs[0], xs[1], xs[2]))
    ans_max = max(ans_max, f(xs[0], xs[1], xs[2]))

print("{:.015f}".format(ans_min))
print("{:.015f}".format(ans_max))
