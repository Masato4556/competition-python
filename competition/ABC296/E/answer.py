## pypyではTLEだが、CythonだとACだった

from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

def dfs(graph, node, visited, stack):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(graph, neighbor, visited, stack)
        stack.append(node)

def solve(graph, transposed_graph):
    # Perform DFS on the original graph to fill the stack
    stack = []
    visited = set()
    for node in graph:
        if node not in visited:
            dfs(graph, node, visited, stack)

    # Perform DFS on the transposed graph in the order given by the stack
    visited = set()
    ans = 0
    while stack:
        node = stack.pop()
        if node not in visited:
            scc = []
            dfs(transposed_graph, node, visited, scc)
            if len(scc) > 1:
                ans += len(scc)

            if scc[0] in G[scc[0]]:
                ans += 1

    return ans


N = int(input())
A = list(map(int, input().split()))

G = defaultdict(list)
G_rev = defaultdict(list)

for i in range(1, N+1):
    G[i].append(A[i-1])
    G_rev[A[i-1]].append(i)


print(solve(G, G_rev))
