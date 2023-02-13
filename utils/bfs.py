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

    def find_shortest_path(this, x, y): # x->yの最短経路を求める
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


# 到達可能かを調べる

# 最長経路を求める

# 経路復元

# 二部グラフ判定

# トポロジカルソート

# サイクル検出