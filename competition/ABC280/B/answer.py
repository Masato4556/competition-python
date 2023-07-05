
N = int(input())
S = list(map(int, input().split()))


ans = []
prev_s = 0
for i in range(N):
    ans.append(str(S[i] - prev_s))
    prev_s = S[i]

print(" ".join(ans))

