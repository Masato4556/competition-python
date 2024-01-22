
N = int(input())
A = list(map(int, input().split()))

prev = [-1] * N
indeg = [0] * N
for i in range(N):
    if A[i] == -1:
        continue

    indeg[A[i]-1] += 1

# print(indeg)
ind = indeg.index(0)


ans = []
for _ in range(N):
    # print(ind)
    ans.append(ind+1)
    ind = A[ind] - 1
ans.reverse()
print(*ans)
