from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

counter = defaultdict(int)

ans = 10**12

for a in A:
    counter[a] += 1

    if counter[a] > counter[ans]:
        ans = a
    elif counter[a] == counter[ans] and a < ans:
        ans = a

    print(ans)
