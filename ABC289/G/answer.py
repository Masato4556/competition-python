n, m = map(int, input().split())
B = list(map(int, input().split()))
B.sort()
C = list(map(int, input().split()))

results = []
for i in range(m):
    results.append(str(max([(B[j] + C[i]) * (n - j) for j in range(n)])))

print(" ".join(results))