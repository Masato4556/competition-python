from collections import deque


H, W = map(int, input().split())

move = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]

target = "snuke"

S = []
s_poses = []
for i in range(H):
    s = input()
    S.append(s)
    for j in range(W):
        if s[j] == "s":
            s_poses.append((i, j))

que = deque([])
for s_pos in s_poses:
    for m in move:
        que.append((s_pos, m, 1))

while que:
    s_pos, m, i = que.popleft()

    if not (0 <= s_pos[0] + m[0] * i < H and 0 <= s_pos[1] + m[1] * i < W):
        continue
    if S[s_pos[0] + m[0] * i][s_pos[1] + m[1] * i] == target[i]:
        if i == 4:
            ans = []
            for j in range(5):
                # ans.append(S[s_pos[0] + m[0] * j][s_pos[1] + m[1] * j])
                ans.append((s_pos[0] + m[0] * j, s_pos[1] + m[1] * j))
            # print("\n".join(ans))
            for r, c in ans:
                print(f"{r+1} {c+1}")
        else:
            que.append((s_pos, m, i+1))
