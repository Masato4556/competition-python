from functools import cmp_to_key
N = int(input())


def f(v1, v2):
    a1, b1 = v1[0]
    a2, b2 = v2[0]
    if a1*(a2+b2) == a2*(a1+b1):
        return -1 if v1[1] < v2[1] else 1
    return -1 if a1*(a2+b2) > a2*(a1+b1) else 1


ans = []
for i in range(N):
    a, b = map(int, input().split())

    ans.append(((a, b), i+1))

ans.sort(key=cmp_to_key(f))
print(*[a[1] for a in ans])
