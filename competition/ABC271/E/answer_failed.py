from collections import defaultdict, deque
import sys

sys.setrecursionlimit(10**6)

INF = 10**18 + 1

class Route:
    def __init__(this, start, end, dist):
        this.start = start
        this.end = end
        this.dist = dist

n, m, k = map(int, input().split())

routes = []
for i in range(m):
    a, b, c = map(int, input().split())
    routes.append(Route(a, b, c))

E = list(map(int, input().split()))

def f(prev, e_ind, dist):
    route = routes[E[e_ind]-1]
    valid = False
    if route.start not in (1, prev):
        return INF

    dist += route.dist
    if route.end == n:
        return dist

    if e_ind >= k:
        return INF

    min_dist = INF
    for i in range(e_ind+1, k):
        min_dist = min(f(route.end, i, dist), min_dist)

    return min_dist

ans = INF
for i in range(k):
    ans = min(f(-1, i, 0), ans)

print(ans if ans != INF else -1)





