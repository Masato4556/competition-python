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


def cumulative_sum(arr):
    cumsum = [0]
    for v in arr:
        cumsum.append(cumsum[-1] + v)
    return cumsum


def solve():
    N = INT()

    odd_pos = []
    even_pos = []
    for _ in range(N):
        x, y = MAP(int)
        x, y = x+y, x-y
        if x % 2 == 0 and y % 2 == 0:
            even_pos.append((x, y))
        else:
            odd_pos.append((x, y))

    odd_pos_x = [x for x, _ in odd_pos]
    odd_pos_y = [y for _, y in odd_pos]
    even_pos_x = [x for x, _ in even_pos]
    even_pos_y = [y for _, y in even_pos]

    odd_pos_x.sort()
    odd_pos_y.sort()
    even_pos_x.sort()
    even_pos_y.sort()

    odd_pos_x_cumsum = cumulative_sum(odd_pos_x)
    odd_pos_y_cumsum = cumulative_sum(odd_pos_y)
    even_pos_x_cumsum = cumulative_sum(even_pos_x)
    even_pos_y_cumsum = cumulative_sum(even_pos_y)

    odd_pos_x.sort(reverse=True)
    odd_pos_y.sort(reverse=True)
    even_pos_x.sort(reverse=True)
    even_pos_y.sort(reverse=True)

    ans = 0
    odd_pos_count = len(odd_pos)
    even_pos_count = len(even_pos)
    if odd_pos_count > 1:
        for i in range(odd_pos_count-1):
            ans += (odd_pos_count-i) * \
                odd_pos_x[i] - odd_pos_x_cumsum[odd_pos_count-i]
            ans += (odd_pos_count-i) * \
                odd_pos_y[i] - odd_pos_y_cumsum[odd_pos_count-i]

    if even_pos_count > 1:
        for i in range(even_pos_count-1):
            ans += (even_pos_count-i) * \
                even_pos_x[i] - even_pos_x_cumsum[even_pos_count-i]
            ans += (even_pos_count-i) * \
                even_pos_y[i] - even_pos_y_cumsum[even_pos_count-i]
    print(ans//2)


solve()
