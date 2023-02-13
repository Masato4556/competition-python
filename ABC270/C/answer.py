from collections import deque

class bfs:
    def __init__(this, n, g):
        this.n = n
        this.g = g

        this.root_par = -2

    def generate_par_and_dist(this, root):
        que = deque([x])

        par = [-1] * this.n
        par[x] = this.root_par
        dist = [-1] * this.n
        dist[x] = 0 
        
        while len(que):
            v = que.popleft()
            for next_v in this.g[v]:
                if par[next_v] != -1 or par[next_v] == this.root_par: continue
                par[next_v] = v
                dist[next_v] = dist[v] + 1
                que.append(next_v)

        return (par, dist)

    def find_shortest_path(this, x, y): # 最短経路を求める
        par, dist = this.generate_par_and_dist(x)

        path = []
        path.append(y)
        t = y
        for _ in range(n):
            if par[t] == this.root_par:
                break
            path.append(par[t])
            t = par[t]

        path.reverse()
        return (path, dist[y])

n, x, y = map(int, input().split())
x -= 1
y -= 1

G = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

b = bfs(n, G)
path, _ = b.find_shortest_path(x, y)

print(" ".join([str(v+1) for v in path]))
