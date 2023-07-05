from collections import defaultdict
from copy import copy

N, K, D = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
AmodD = defaultdict(list)
for a in A:
    AmodD[a%D].append(a)

dp = [defaultdict(list) for _ in range(K)]
for i in range(D):
    count = defaultdict(int)
    count[i] = 1
    if len(AmodD[i]):
        dp[0][i].append((AmodD[i][0], count))

for i in range(K-1):
    for j, arr in dp[i].items():
        for v, dic in arr:
            if v == -1: continue
            for k in range(D):
                if dic[k] >= len(AmodD[k]): continue
                next_v = v + AmodD[k][dic[k]]

                if len(dp[i+1][(j+k)%D]) != 0 and next_v < dp[i+1][(j+k)%D][0][0]: continue
                
                next_dic = copy(dic)
                next_dic[k] += 1

                if len(dp[i+1][(j+k)%D]) != 0 and next_v == dp[i+1][(j+k)%D][0][0]: 
                    dp[i+1][(j+k)%D].append((next_v, next_dic))
                else:
                    dp[i+1][(j+k)%D] = [(next_v, next_dic)]

print(dp[-1][0][0][0] if len(dp[-1][0]) else -1)
