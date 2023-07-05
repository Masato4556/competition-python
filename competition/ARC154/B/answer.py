from collections import defaultdict

N = int(input())
S = input()
T = input()

for s, t in zip(sorted(S), sorted(T)):
    if s != t:
        print(-1)
        exit()

s_i = N-1
t_i = N-1
c = 0 # 動かす必要のない文字の数
while s_i >= 0 and t_i >= 0:
    if S[s_i] == T[t_i]: 
        s_i -= 1
        c += 1
    t_i -= 1

print(N-c)
