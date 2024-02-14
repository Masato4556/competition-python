from bisect import bisect_left

D = int(input())

X = [0]
i = 0
while X[-1] <= D:
    i += 1
    X.append(i ** 2)

# print(X)

ans = float("inf")
for x in X:
    yi = bisect_left(X, D-x)
    ans = min(ans, abs(D-x-X[yi]))
    if yi != 0:
        ans = min(ans, abs(D-x-X[yi-1]))

print(ans)
