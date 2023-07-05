from random import randint

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(set)

    def add_edge(self, u, v):
        self.graph[u].add(v)

    def dfs(self, v, visited, stack):
        visited.add(v)
        for i in self.graph[v]:
            if i not in visited:
                self.dfs(i, visited, stack)
        stack.append(v)

    def transpose(self):
        g = Graph()
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def scc(self):
        visited = set()
        stack = []
        for v in self.graph:
            if v not in  visited:
                self.dfs(v, visited, stack)
        transposed_graph = self.transpose()
        visited = set()
        sccs = []
        while stack:
            v = stack.pop()
            if v not in visited:
                scc = []
                transposed_graph.dfs(v, visited, scc)
                sccs.append(scc)
        return sccs



N = 10**5

A = [randint(1, N) for _ in range(N)]

print(A)

G = [-1 for _ in range(N+1)]

g = Graph()
for i in range(1, N+1):
    g.add_edge(i, A[i-1])

ans = 0
for e in g.scc():
    if len(e) > 1:
        ans += len(e)
        continue

    if e[0] in g.graph[e[0]]:
        ans += 1
print(ans)


