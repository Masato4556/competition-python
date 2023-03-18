def count_ones(n):
    count = 0
    while n > 0:
        if n & 1:
            count += 1
        n >>= 1
    return count

N = int(input())
S = input()
T = input()

cnt = 0
for i in range(N):
    if S[i] == T[i]: continue
    cnt += 1

if cnt % 2 != 0: 
    print(-1)
    exit()

s_select_cnt = cnt//2
t_select_cnt = cnt//2

ans = []
for i in range(N):
    if S[i] != T[i]:
        if s_select_cnt == 0:
            ans.append(T[i])
        elif t_select_cnt == 0:
            ans.append(S[i])
        else:
            ans.append("0")
            if S[i] == "0":
                s_select_cnt -= 1
            else:
                t_select_cnt -= 1
    else:
       ans.append("0")

print("".join(ans))