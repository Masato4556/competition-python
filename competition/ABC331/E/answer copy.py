from collections import deque
N, M, L = map(int, input().split())
A = [(v, i)for i, v in enumerate(map(int, input().split()))]
B = [(v, i)for i, v in enumerate(map(int, input().split()))]
A.sort(reverse=True)
B.sort(reverse=True)

excludes = set()
for _ in range(L):

    excludes.add(tuple(map(lambda x: int(x)-1, input().split())))

# print(A)
# print(B)
# print(excludes)
que = deque([(0, 0)])

ans = 0
done = set()
while que:
    a_i, b_i = que.popleft()
    if (A[a_i][1], B[b_i][1]) in done:
        continue
    done.add((a_i, b_i))
    if a_i >= N or b_i >= M:
        continue
    if (A[a_i][1], B[b_i][1]) in excludes:
        que.append((a_i+1, b_i))
        que.append((a_i, b_i+1))
        continue
    ans = max(ans, A[a_i][0] + B[b_i][0])
print(ans)
