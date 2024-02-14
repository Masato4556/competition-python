import sys
INF = float('inf')
sys.setrecursionlimit(10**9)
def f(x): return x
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(func): return map(func, input().split())
def LIST(func=f): return list(map(func,  input().split()))
def TUPLE(func=f): return tuple(map(func, input().split()))
def GRID(n, func=f): return [input() for _ in range(n)]
def ZIP(n, func=f): return zip(*(MAP(func) for _ in range(n)))


N = INT()
G = GRID(N)

row_counts = []
col_counts = []

for i in range(N):
    row_counts.append(G[i].count("o"))

for i in range(N):
    cnt = 0
    for j in range(N):
        cnt += 1 if G[j][i] == "o" else 0
    col_counts.append(cnt)

# print(G)
# print(row_counts)
# print(col_counts)

ans = 0
for i in range(N):
    for j in range(N):
        if G[i][j] == "o":
            ans += (row_counts[i] - 1) * (col_counts[j] - 1)

print(ans)
