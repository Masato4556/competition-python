from scipy.special import comb

N = int(input())
A = list(map(int, input().split()))

cnt = [0] * (N+1)
for a in A:
    cnt[a] += 1

base = 0
for i in range(1, N+1):
    base += comb(cnt[i], 2, exact=True)

for i in range(N):
    ans = 0
    a_cnt = cnt[A[i]]
    print(base - comb(a_cnt, 2, exact=True) + comb(a_cnt-1, 2, exact=True))