from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

g = defaultdict(list)

# iをAiの値でグルーピング
for i in range(N):
    g[A[i]].append(i)

ans = 0
for inds in g.values():
    index_num = len(inds)
    if index_num < 2:
        continue
    
    for i in range(index_num):
        for k in range(i+1, index_num):
            # Aiの値ごとの、i<j<k　かつ　Ai != Aj となるjの個数
            ans += inds[k]-inds[i] - (k-i)

print(ans)