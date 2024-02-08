
N, Q = map(int, input().split())
P = [input() for _ in range(N)]

# print(P)

lt = [[0 for _ in range(N+1)] for _ in range(N+1)]
rt = [[0 for _ in range(N+1)] for _ in range(N+1)]
rb = [[0 for _ in range(N+1)] for _ in range(N+1)]
lb = [[0 for _ in range(N+1)] for _ in range(N+1)]
for y in range(N):
    for x in range(N):
        if P[y][x] == "B":
            lt[y+1][x+1] += 1
        lt[y+1][x+1] += lt[y][x+1]
        lt[y+1][x+1] += lt[y+1][x]
        lt[y+1][x+1] -= lt[y][x]

        if P[y][N-1-x] == "B":
            rt[y+1][x+1] += 1
        rt[y+1][x+1] += rt[y][x+1]
        rt[y+1][x+1] += rt[y+1][x]
        rt[y+1][x+1] -= rt[y][x]

        if P[N-1-y][x] == "B":
            lb[y+1][x+1] += 1
        lb[y+1][x+1] += lb[y][x+1]
        lb[y+1][x+1] += lb[y+1][x]
        lb[y+1][x+1] -= lb[y][x]

        if P[N-1-y][N-1-x] == "B":
            rb[y+1][x+1] += 1
        rb[y+1][x+1] += rb[y][x+1]
        rb[y+1][x+1] += rb[y+1][x]
        rb[y+1][x+1] -= rb[y][x]

# print(lt)
# print(rt)
# print(rb)
# print(lb)

for _ in range(Q):
    y0, x0, y1, x1 = map(int, input().split())

    width = x1 - x0 + 1
    height = y1 - y0 + 1
    x_offset = [(N - (x0 % N)) % N, (x1+1) % N]
    y_offset = [(N - (y0 % N)) % N, (y1+1) % N]
    x_repeat_count = (width - sum(x_offset)) // N
    y_repeat_count = (height - sum(y_offset)) // N

    ans = x_repeat_count * y_repeat_count * rb[N][N]
    ans += rb[y_offset[0]][x_offset[0]]
    ans += lb[y_offset[0]][x_offset[1]]
    ans += rt[y_offset[1]][x_offset[0]]
    ans += lt[y_offset[1]][x_offset[1]]
    ans += x_repeat_count * rb[y_offset[0]][N]
    ans += x_repeat_count * rt[y_offset[1]][N]
    ans += y_repeat_count * rb[N][x_offset[0]]
    ans += y_repeat_count * lb[N][x_offset[1]]

    # print(x_repeat_count, y_repeat_count, x_offset, y_offset)
    # print(x_repeat_count * y_repeat_count * rb[N][N])
    # print(
    #     rb[y_offset[0]][x_offset[0]],
    #     lb[y_offset[0]][x_offset[1]],
    #     rt[y_offset[1]][x_offset[0]],
    #     lt[y_offset[1]][x_offset[1]])
    # print(x_repeat_count * rb[y_offset[0]][N],
    #       x_repeat_count * rt[y_offset[1]][N],
    #       y_repeat_count * rb[N][x_offset[0]],
    #       y_repeat_count * lb[N][x_offset[1]])

    print(ans)
