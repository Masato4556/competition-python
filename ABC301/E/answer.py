
H, W, T = map(int, input().split())

A = []
e_poses = []
for h in range(H):
    A.append(input())

    for w in range(W):
        if A[h][w] == "S":
            s_pos = (h, w)
        elif A[h][w] == "G":
            g_pos = (h, w)
        elif A[h][w] == "o":
            e_poses.append((h, w))

print(s_pos, g_pos, e_poses)

# スタートとゴールと各エサの間の距離を求めて、同行するのかな。
# 単純にやると計算量がとてつもなく大きくなりそうだが、
# グリッドが最大で 300 x 300、最大ノード数が20(スタート、ゴール、エサが最大で18)なのでなんとかなる？
