T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    S = input()

    ans = 0

    all_d = {"0": 0, "1": 0, "?": 0}
    d = {"0": 0, "1": 0, "?": 0}
    for i in range(N):
        if i < K:
            d[S[i]] += 1
        all_d[S[i]] += 1
    
    if d["1"] + d["?"] == K and all_d["1"] - d["1"] == 0:
        ans += 1

    for i in range(1, N-K+1):
        d[S[i-1]] -= 1
        d[S[i+K-1]] += 1

        if d["1"] + d["?"] == K and all_d["1"] - d["1"] == 0:
            ans += 1

    print("Yes" if ans == 1 else "No")
        /k/