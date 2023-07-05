
S = input()
T = input()

len_S = len(S)
len_T = len(T)


dp = [set() for _ in range(len_T)]

for i in range(len_S):
    if S[i] == T[0] or S[i] == "?":
        dp[0].add(i)

for i in range(1, len_T):
    for j in dp[i-1]:
        jj = j+1
        if jj >= len_S:
            continue
        if S[jj] != T[i] and S[jj] != "?":
            continue

        
        
        dp[i].add(jj)

if len(dp[-1]) <= 0:
    print("UNRESTORABLE")
    exit()

ans = []
ind = len_S - 1
flg = True
while ind >= 0:
    if ind in dp[-1] and flg:
        flg = False
        for i in range(len_T-1, -1, -1):
            ans.append(T[i])
            ind -= 1
    else:
        ans.append("a" if S[ind] == "?" else S[ind])
        ind -= 1

ans.reverse()
print("".join(ans))
