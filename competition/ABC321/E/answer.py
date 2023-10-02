
def countChildren(x, d, n):
    if d < 0 or x < 1:
        return 0

    max_c = min((x+1) * (2**d) - 1, n)
    min_c = x * (2**d)
    return max(max_c-min_c + 1, 0)


T = int(input())
for _ in range(T):
    n, x, k = map(int, input().split())

    ans = countChildren(x, k, n)
    prev_x = x
    x //= 2
    k -= 1
    while x > 0:
        ans += countChildren(x, k, n) - countChildren(prev_x, k-1, n)
        prev_x = x
        x //= 2
        k -= 1

    print(ans)
