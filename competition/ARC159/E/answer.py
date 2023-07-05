
# string
s = input()

# int
n = int(input())

# list
a = list(map(int, input().split()))

# map
n, m = map(int, input().split())

# 有向グラフ
G = [set() for _ in range(n)]
degs = [0 for _ in range(n)]
for _ in range(m):
    u, v = map(lambda x: int(x)-1, input().split())
    G[u].add(v)
    degs[u] += 1
