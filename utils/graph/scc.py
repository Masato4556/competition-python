## https://deus-ex-machina-ism.com/?p=20829

from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

def dfs(graph, node, visited, stack):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(graph, neighbor, visited, stack)
        stack.append(node)

def kosaraju_scc(graph, transposed_graph):
    # Perform DFS on the original graph to fill the stack
    stack = []
    visited = set()
    for node in graph:
        if node not in visited:
            dfs(graph, node, visited, stack)

    # Perform DFS on the transposed graph in the order given by the stack
    visited = set()
    scc_list = []
    while stack:
        node = stack.pop()
        if node not in visited:
            scc = []
            dfs(transposed_graph, node, visited, scc)
            scc_list.append(scc)

    return scc_list

## ==========================================================================

from random import randint
N = 20
A = [randint(1, N) for _ in range(N)]

G = defaultdict(list)
G_rev = defaultdict(list)

for i in range(1, N+1):
    G[i].append(A[i-1])
    G_rev[A[i-1]].append(i)

print(kosaraju_scc(G, G_rev))



