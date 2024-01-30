
N, M = map(int, input().split())
X = list(map(int, input().split()))

# print(N, M)
# print(X)

root = []
better_root = []
dist = [[-1 for _ in range(2)] for _ in range(M-1)]

uniq_X = set(X)

# print(uniq_X)

target = -1


ans = 0
for i in range(M-1):
    lower = min(X[i], X[i+1])
    higher = max(X[i], X[i+1])
    # print(lower, higher)

    root.append((lower, higher))
    dist[i][0] = higher - lower
    dist[i][1] = N - higher + lower
    better_root.append(0 if dist[i][0] < dist[i][1] else 1)
    # print(higher - lower, N - higher + lower)
    ans += min(higher - lower, N - higher + lower)

# print(root)
# print([dist[i] for i in range(M-1)])
# print(better_root)

target = -1
max_lower_dist = 0
for i in range(M-1):
    if min(dist[i]) > max_lower_dist:
        max_lower_dist = min(dist[i])
        target = i

print(target)
ans = float('inf')
for i in range(target,  target+1):
    ans_i = 0
    for j in range(M-1):
        lower, higer = root[j]
        if lower <= i < higer:
            ans_i += dist[j][1]
        else:
            ans_i += dist[j][0]
    # print(i, ans_i)
    ans = min(ans, ans_i)

print(ans)
