
N, M = map(int, input().split())
X = list(map(lambda x: int(x)-1, input().split()))

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
    root.append((lower, higher))
    dist[i][0] = higher - lower
    dist[i][1] = N - higher + lower


diff = [0] * (N+1)
for i in range(M-1):
    lower, higer = root[i]

    diff[lower] += dist[i][1]
    diff[higher] -= dist[i][1]

    diff[0] += dist[i][0]
    diff[lower] -= dist[i][0]
    diff[higher] += dist[i][0]
    diff[N] -= dist[i][1]

ans = [0] * (N)
ans[0] = diff[0]
for i in range(1, N):
    ans[i] = ans[i-1] + diff[i]

# print(diff)
# print(ans)
print(min(ans))
