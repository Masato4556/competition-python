def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    g = gcd(a, b)
    return a // g * b


def f(v, div):
    mod = v % div
    return (div - mod) % div


INF = 10 ** 20

N, a, b, c = map(int, input().split())
A = list(map(int, input().split()))


ab = lcm(a, b)
bc = lcm(c, c)
ca = lcm(c, a)
abc = lcm(ab, bc)
div = [a, b, c, ab, bc, ca, abc]
# div = [a]

min_cnt = [INF] * 7
inds = [set() for _ in range(7)]

min_a, min_b, min_c = INF, INF, INF
min_ab, min_bc, min_ca = INF, INF, INF
min_abc = INF
for i in range(N):
    for j in range(7):
        temp = f(A[i], div[j])
        if temp < min_cnt[j]:
            min_cnt[j] = temp
            inds[j] = set()
        if temp == min_cnt[j]:
            inds[j].add(i)

# print(A)
# print(div)
# print(min_cnt)
# print(inds)

ans = min_cnt[6]

l = [(0, 4), (1, 5), (2, 3)]

# print(ans)
for p, q in [(0, 4), (1, 5), (2, 3)]:
    if len(inds[p] ^ inds[q]) or len(inds[p] | inds[q]) >= 2:
        # if len(inds[p]) != 1 or len(inds[q]) != 1 or len(inds[p] | inds[q]) != 1:
        ans = min(ans, min_cnt[p] + min_cnt[q])
# print(ans)
if len(inds[0] ^ inds[1]) and len(inds[1] ^ inds[2]) and len(inds[2] ^ inds[0]):
    ans = min(ans, min_cnt[0] + min_cnt[1] + min_cnt[2])

print(ans)
