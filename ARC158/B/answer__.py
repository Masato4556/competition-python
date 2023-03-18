def f(xi, xj, xk):
    return (xi + xj + xk) / (xi * xj * xk)

n = int(input())
x = list(map(int, input().split()))

x_plus = [v for v in x if v > 0]
x_minus = [v for v in x if v < 0]

x_plus.sort()
x_minus.sort()

ans_min = 10000
ans_max = -10000

if len(x_plus) >= 3:
    ans_min = min(ans_min, f(x_plus[-1], x_plus[-2], x_plus[-3]))
    ans_max = max(ans_max, f(x_plus[0], x_plus[1], x_plus[2]))

if len(x_minus) >= 3:
    ans_min = min(ans_min, f(x_minus[0], x_minus[1], x_minus[2]))
    ans_max = max(ans_max, f(x_minus[-1], x_minus[-2], x_minus[-3]))

if len(x_plus) >= 2 and len(x_minus) >= 1 :
    ans_min = min(ans_min, f(x_plus[0], x_plus[1], x_minus[-1]))
    ans_max = max(ans_max, f(x_plus[0], x_plus[1], x_minus[0]))

if len(x_plus) >= 1 and len(x_minus) >= 2 :
    ans_min = min(ans_min, f(x_plus[0], x_minus[-1], x_minus[-2]))
    ans_max = max(ans_max, f(x_plus[-1], x_minus[0], x_minus[1]))

print("{:.020f}".format(ans_min))
print("{:.020f}".format(ans_max))
