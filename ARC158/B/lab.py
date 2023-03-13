from itertools import combinations
import random

def f(xi, xj, xk):
    return (xi + xj + xk) / (xi * xj * xk)

# X = [-6000, -5000, -4000, -3000, -2000, -1000]
limit = 10**6
X = [random.randint(-1 * limit, limit) for _ in range(10)]
X = [x for x in X if x != 0]
print(X)

ans_min = 10000
ans_max = -10000

for xs in combinations(X, 3):
    ans_min = min(ans_min, f(xs[0], xs[1], xs[2]))
    ans_max = max(ans_max, f(xs[0], xs[1], xs[2]))
    print(xs, "{:.015f}".format(ans_min))

print("{:.015f}".format(ans_min))
print("{:.015f}".format(ans_max))

print("=======")


x_plus = [v for v in X if v > 0]
x_minus = [v for v in X if v < 0]

x_plus.sort()
x_minus.sort()

ans_min = 10000
ans_max = -10000

if len(x_plus) >= 3:
    ans_min = min(ans_min, f(x_plus[-1], x_plus[-2], x_plus[-3]))
    ans_max = max(ans_max, f(x_plus[0], x_plus[1], x_plus[2]))
    print("1", "{:.015f}".format(ans_min))

if len(x_minus) >= 3:
    ans_min = min(ans_min, f(x_minus[0], x_minus[1], x_minus[2]))
    ans_max = max(ans_max, f(x_minus[-1], x_minus[-2], x_minus[-3]))
    print("2", "{:.015f}".format(ans_min))

if len(x_plus) >= 2 and len(x_minus) >= 1 :
    ans_min = min(ans_min, f(x_plus[0], x_plus[1], x_minus[-1]))
    ans_max = max(ans_max, f(x_plus[0], x_plus[1], x_minus[0]))
    print("3", "{:.015f}".format(ans_min))

if len(x_plus) >= 1 and len(x_minus) >= 2 :
    ans_min = min(ans_min, f(x_plus[0], x_minus[-1], x_minus[-2]))
    ans_max = max(ans_max, f(x_plus[-1], x_minus[0], x_minus[1]))
    print("4", "{:.015f}".format(ans_min))

print("{:.015f}".format(ans_min))
print("{:.015f}".format(ans_max))

