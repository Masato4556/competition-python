from collections import deque
N = int(input())

low_edge_to_connectio_no = dict()
hige_edges_to_connection_no = dict()
for i in range(N):
    a, b = map(lambda x: int(x)-1, input().split())
    low_edge = min(a, b)
    high_edge = max(a, b)
    low_edge_to_connectio_no[low_edge] = i
    hige_edges_to_connection_no[high_edge] = i

que = deque()

for i in range(2*N):
    if i in low_edge_to_connectio_no:
        que.append(low_edge_to_connectio_no[i])
    else:
        t = que.pop()
        if hige_edges_to_connection_no[i] != t:
            print("Yes")
            exit()


print("No")
