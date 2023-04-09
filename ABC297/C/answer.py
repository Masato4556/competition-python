
H, W = map(int, input().split())

for _ in range(H):
    S = list(input())

    for i in range(1, W):
        if S[i-1] == "T" and S[i] == "T":
            S[i-1], S[i] = "P", "C"

    print("".join(S))

