from itertools import combinations
def f(xi, xj, xk):
    return (xi + xj + xk) / (xi * xj * xk)

n = int(input())
X = list(map(int, input().split()))

def f(xi, xj, xk):
    return (xi + xj + xk) / (xi * xj * xk)

ans_min = 10000
ans_max = -10000

for xs in combinations(X, 3):
    ans_min = min(ans_min, f(xs[0], xs[1], xs[2]))
    ans_max = max(ans_max, f(xs[0], xs[1], xs[2]))

print("{:.020f}".format(ans_min))
print("{:.020f}".format(ans_max))
