

INF = 10**18
H, W, K = map(int, input().split())

S = []
for _ in range(H):
    temp = []
    for c in input():
        if c == "x":
            temp.append(-INF)
        elif c == "o":
            temp.append(1)
        else:
            temp.append(0)
    S.append(temp)


# for s in S:
#     print(s)

max_cnt = -INF

if K <= W:
    for y in range(H):
        cur_cnt = sum([S[y][i] for i in range(K)])
        if cur_cnt > max_cnt:
            max_cnt = cur_cnt
        for x in range(W-K):
            cur_cnt -= S[y][x]
            cur_cnt += S[y][x+K]
            if cur_cnt > max_cnt:
                max_cnt = cur_cnt

if K <= H:
    for x in range(W):
        cur_cnt = sum([S[i][x] for i in range(K)])
        if cur_cnt > max_cnt:
            max_cnt = cur_cnt
        for y in range(H-K):
            cur_cnt -= S[y][x]
            cur_cnt += S[y+K][x]
            if cur_cnt > max_cnt:
                max_cnt = cur_cnt

print(-1 if max_cnt < 0 else K-max_cnt)
