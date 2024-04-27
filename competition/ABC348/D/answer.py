import sys
from collections import deque, defaultdict
INF = float('inf')
sys.setrecursionlimit(10**9)
def f(x): return x
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(func=f): return map(func, input().split())
def LIST(func=f): return list(map(func, input().split()))
def TUPLE(func=f): return tuple(map(func, input().split()))
def GRID(n): return [input() for _ in range(n)]
def ZIP(n, func=f): return zip(*(MAP(func) for _ in range(n)))


def next_position(pos):
    return ((pos[0], pos[1]+1), (pos[0], pos[1]-1), (pos[0]+1, pos[1]), (pos[0]-1, pos[1]))


H, W = MAP(int)
A = GRID(H)
N = INT()
medicines = []
for _ in range(N):
    r, c, e = MAP(int)
    r -= 1
    c -= 1
    medicines.append((r, c, e))

start_pos = [-1, -1]
goal_pos = [-1, -1]
for i in range(H):
    for j in range(W):
        if A[i][j] == "S":
            start_pos = (i, j)
        elif A[i][j] == "T":
            goal_pos = (i, j)

positions = []
for medicine in medicines:
    positions.append((medicine[0], medicine[1]))
positions.append(goal_pos)

conv2Index = {v: i for i, v in enumerate(positions)}

if start_pos not in conv2Index:
    print("No")
    exit()

G = [set() for _ in range(N+1)]

for i in range(N):
    dist = [[-1 for _ in range(W)] for _ in range(H)]
    queue = deque([(positions[i][0], positions[i][1])])
    dist[positions[i][0]][positions[i][1]] = 0

    while queue:
        pos = queue.popleft()
        for next_pos in next_position(pos):
            if next_pos[0] < 0 or next_pos[0] >= H or next_pos[1] < 0 or next_pos[1] >= W:
                continue
            if A[next_pos[0]][next_pos[1]] == "#":
                continue
            if dist[next_pos[0]][next_pos[1]] != -1:
                continue
            dist[next_pos[0]][next_pos[1]] = dist[pos[0]][pos[1]] + 1
            if dist[next_pos[0]][next_pos[1]] > medicines[i][2]:
                continue
            if next_pos in conv2Index:
                G[i].add(conv2Index[next_pos])
            queue.append(next_pos)

queue = deque([conv2Index[start_pos]])
accessed = [0] * (N+1)
accessed[conv2Index[start_pos]] = 1
while queue:
    v = queue.popleft()
    for next_v in G[v]:
        if accessed[next_v]:
            continue
        if next_v == N:
            print("Yes")
            exit()
        queue.append(next_v)
        accessed[next_v] = 1
print("No")
