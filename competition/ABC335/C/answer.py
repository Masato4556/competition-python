from collections import deque

N, Q = map(int, input().split())

offset = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1)
}

que = [(i, 0) for i in range(N, 0, -1)]

for _ in range(Q):
    q1, q2 = input().strip().split()

    if q1 == "1":
        next_pos = (que[-1][0]+offset[q2][0], que[-1][1]+offset[q2][1])
        que.append(next_pos)
        # print(que)
    else:
        p = int(q2)
        # print(que, p)
        print(*que[-p])
