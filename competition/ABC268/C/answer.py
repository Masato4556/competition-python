
n = int(input())
P = list(map(int, input().split()))

res = [0 for _ in range(n)]

for i in range(0, n):
    p = P[i-1]
    res[(p-i-1) % n] += 1
    res[(p-i) % n] += 1
    res[(p-i+1) % n] += 1

print(max(res))
