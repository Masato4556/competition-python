
from collections import Counter


N, Q = map(int, input().split())
A = list(map(int, input().split()))

counter = Counter(A)

ans = 0
while True:
    if counter[ans] == 0:
        break
    ans += 1

# print(counter)
for _ in range(Q):
    i, x = map(int, input().split())
    i -= 1

    # print(A[i], x)

    prev = A[i]
    counter[prev] -= 1
    counter[x] += 1
    A[i] = x
    # print(counter)

    if counter[prev] == 0 and prev < ans:
        ans = prev
    elif x == ans:
        while True:
            if counter[ans] == 0:
                break
            ans += 1
    print(ans)
