from collections import defaultdict

n, m, t = map(int, input().split())
A = list(map(int, input().split()))
B = defaultdict(int)
for _ in range(m): 
    x, y = map(int, input().split())
    B[x-1] = y

ans = "Yes"
for i in range(n-1):
    t += B[i]
    t -= A[i]
    if t <= 0:
        ans = "No"
        break

print(ans)