A, B = map(int, input().split())
A, B = max(A, B), min(A, B)
ans = 0
while A != B:
    if A % B == 0:
        ans += A // B - 1
        break
    q, r = divmod(A, B)
    ans += q
    A, B = B, r

print(ans)