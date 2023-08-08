from collections import deque
MOD = 998244353
S = input()

len_s = len(S)

que = deque([(0, 0)])

ans = 0
while len(que):
    v, i = que.pop()

    if i >= len_s:
        continue
    if i == len_s-1 and v == 0:
        ans += 1
        ans %= MOD

    if v < 0:
        continue
    if v > len_s - i:
        continue

    if S[i] == "(":
        que.append((v+1, i+1))
    elif S[i] == ")":
        if v-1 < 0:
            continue
        que.append((v-1, i+1))
    else:
        if v-1 > 0:
            que.append((v-1, i+1))
        que.append((v+1, i+1))

print(ans)
