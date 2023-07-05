n, l = map(int, input().split())
a = list(map(int, input().split()))

if l < n:
    print("No")
    exit()

ind = 0
while ind < n:
    if a[ind] + 1 > l: break
    l -= a[ind] + 1
    ind += 1

print("Yes" if a[ind:].count(2) <= l // 2 else "No")
