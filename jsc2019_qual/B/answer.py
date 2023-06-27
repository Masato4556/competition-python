
MOD = 10**9+7
N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt1 = 0
cnt2 = 0
for i in range(N):
    for j in range(N):
        # print(i, j, A[i], A[j])
        if A[i] <= A[j]:
            continue

        cnt2 += 1
        if i < j:
            cnt1 += 1

ans = cnt1 * K % MOD
ans += cnt2 * ((0+K-1) * K // 2) % MOD
ans %= MOD

print(ans)
