
S = input()
T = input()

len_S = len(S)
len_T = len(T)

dp = [[0] * len_S for _ in range(len_T)]

for i in range(len_T):
    for j in range(i, len_S):
        if S[j] != T[i] and S[j] != "?":
            continue

        if i != 0 and not dp[i-1][j-1]:
            continue
        
        dp[i][j] = 1

if dp[-1].count(1) == 0:
    print("UNRESTORABLE")
    exit()

ans = []
ind = len_S - 1
flg = False
while ind >= 0:
    if dp[-1][ind] == 1:
        for i in range(len_T-1, -1, -1):
            ans.append(T[i])
            ind -= 1

    ans.append("a" if S[ind] == "?" else S[ind])
    ind -= 1

ans.reverse()
print("".join(ans))
