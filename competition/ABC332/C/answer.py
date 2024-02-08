
N, M = map(int, input().split())
S = input().split("0")

ans = 0
for S_i in S:
    counter = [0, 0]
    for c in S_i:
        counter[int(c)-1] += 1

    ans = max(ans, counter[1] + max(0, counter[0] - M))

print(ans)
