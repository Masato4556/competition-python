import sys
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


def solve():
    N = INT()

    odd_pos = []
    even_pos = []
    for _ in range(N):
        x, y = MAP(int)
        if (x+y) % 2 == 0:
            even_pos.append((x, y))
        else:
            odd_pos.append((x, y))

    ans = 0
    odd_pos_count = len(odd_pos)
    even_pos_count = len(even_pos)
    if odd_pos_count > 1:
        for i in range(odd_pos_count):
            for j in range(i+1, odd_pos_count):
                ans += max(abs(odd_pos[i][0] - odd_pos[j][0]),
                           abs(odd_pos[i][1] - odd_pos[j][1]))

    if even_pos_count > 1:
        for i in range(even_pos_count):
            for j in range(i+1, even_pos_count):
                ans += max(abs(even_pos[i][0] - even_pos[j][0]),
                           abs(even_pos[i][1] - even_pos[j][1]))
    print(ans)


solve()
