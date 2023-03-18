

n, l = map(int, input().split())
a = list(map(int, input().split()))


t = [[None for _ in range(n)] for _ in range(n)]
s = []

for i in range(n):
    for j in range(n):
        if i < j:
            r_t = a[j] - a[i]
            l_t = a[i] + a[j]
        elif i > j:
            r_t = (l - a[i]) + (l - a[j])
            l_t = a[i] - a[j]
        else:
            r_t = 2 * (l - a[i])
            l_t = 2 * a[i]
        t[i][j] = (r_t, l_t)

for i in range(n):
    sum