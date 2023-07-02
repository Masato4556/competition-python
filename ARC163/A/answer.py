T = int(input())

for _ in range(T):
    N = int(input())
    S = input()

    ans = "No"
    # print(S)
    for i in range(1, N):
        ans = "Yes" if i < (N-i) else "No"
        for j in range(i):
            if i+j >= N:
                break
            # print(f"j: {j}")
            if S[j] < S[i+j]:
                ans = "Yes"
                break
            elif S[j] == S[i+j]:
                continue
            else:
                ans = "No"
                break
        # print(ans)
        if ans == "Yes":
            break
    print(ans)
