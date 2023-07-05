from collections import deque

# 参考: https://qiita.com/zawawahoge/items/8bbd4c2319e7f7746266
def popcount(x):
    x = x - ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 0x0000007f

N = int(input())

S = [input() for _ in range(N)]
G = [set() for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j: continue
        if S[i][-1] != S[j][0]: continue

        G[i].add(j)


dp = [[0] * N for _ in range(2**N)]
que = deque([])
for i in range(N):
    que.append((1<<i, i))

ans = set()
while len(que):
    s, v = que.popleft()
    flag = True
    for next_v in G[v]:
        if s & (1 << next_v): continue
        if dp[s|1<<next_v][next_v]: continue
        que.append((s|(1<<next_v), next_v))
        flag = False
    if flag:
        dp[s][v] = 1 

for i in range(2**N):
    if 1 not in dp[i]: continue
    if popcount(i) % 2 == 1:
        print("First")
        exit()

print("Second")
    