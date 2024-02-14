
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = [0] * N
all_diff = 0
for i in B:
    ai = A[i] + diff[i] + all_diff
    div = ai // N
    mod = ai % N
    diff[i] -= ai
    all_diff += div
    for j in range(1, mod+1):
        diff[(i+j) % N] += 1

    # print(diff, all_diff)

print(*[x+y+all_diff for x, y in zip(A, diff)])
