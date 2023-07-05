from collections import defaultdict

H, W, N, h, w = map(int, input().split())

h_sets = []
w_sets = [set() for _ in range(W)]
s_h = [set() for _ in range(H+1)]
s_w = [set() for _ in range(W+1)]
s_h_r = [set() for _ in range(H+1)]
s_w_r = [set() for _ in range(W+1)]


for i in range(H):
    r = list(map(int, input().split()))
    h_sets.append(set(r)) 
    for i in range(W):
        w_sets[i].add(r[i])

for i in range(H):
    s_h[i+1] |= s_h[i] | h_sets[i]

h_sets.reverse()
for i in range(H):
    s_h_r[i+1] |= s_h_r[i] | h_sets[i]

for i in range(W):
    s_w[i+1] |= s_w[i] | w_sets[i]

w_sets.reverse()
for i in range(W):
    s_w_r[i+1] |= s_w_r[i] | w_sets[i]

for k in range(H-h+1):
    ans = []
    for l in range(W-w+1):
        ans.append(len(s_h[k] | s_h_r[H-k-h] | s_w[l] | s_w_r[W-l-w]))
    
    print(*ans)
