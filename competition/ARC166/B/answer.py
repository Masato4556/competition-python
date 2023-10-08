from itertools import product


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
bc = lcm(b, c)
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

print(A)
print(div)
print(min_cnt)
print(inds)

ans = min_cnt[6]

for p, q in [(0, 4), (1, 5), (2, 3)]:
    for p_i, q_i in product(inds[p], inds[q]):
        if p_i != q_i:
            ans = min(ans, min_cnt[p] + min_cnt[q])
            break

for a_i, b_i, c_i in product(inds[0], inds[1], inds[2]):
    if a_i != b_i and b_i != c_i and c_i != a_i:
        ans = min(ans, min_cnt[0] + min_cnt[1] + min_cnt[2])
        break


print(ans)
