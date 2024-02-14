
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = [0] * N
all_diff = 0
for i in B:
    d = 0
    for j in range(i+1):
        d += diff[j]
    d += all_diff
    ai = A[i] + d
    div = ai // N
    mod = ai % N
    diff[i] -= ai

    end = (i+mod) % N
    if (i+mod) % N > i:
        diff[i+1] += 1
        if end != N-1:
            diff[end+1] -= 1
    else:
        diff[0] += 1
        diff[end+1] -= 1
        diff[i+1] += 1
    all_diff += div

    # print(diff, all_diff)

print(*[x+y+all_diff for x, y in zip(A, diff)])
