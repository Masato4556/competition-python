
A = list(map(int, input().split()))

ans = 0
add = 1
for i in range(64):
    if i != 0:
        add *= 2
    if A[i] == 1:
        ans += add
print(ans)
