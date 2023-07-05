n = int(input())
X = list(map(int, input().split()))
X.sort()
total = 0
for i in range(n, len(X)-n):
    total += X[i]

print(total / (len(X) - 2 * n))
