from itertools import combinations

def f(xi, xj, xk):
    return (xi + xj + xk) / (xi * xj * xk)

n = int(input())
x = list(map(int, input().split()))

xx = [1/(v[0]*v[1]) for v in combinations(x, 2)]

print("{:.015f}".format(sum(xx[0:3])))
print("{:.015f}".format(sum(xx[-4:-1])))