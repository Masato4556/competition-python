

N, M = map(int, input().split())
A = list(map(int, input().split()))

replaced = list(range(1, N+1))
aa = [1] * M
for i in range(M):
    a = A[i]
    if replaced[a-1] == 1:
        aa[i] = replaced[a] 
    elif replaced[a] == 1: 
        aa[i] = replaced[a-1] 
    
    replaced[a-1], replaced[a] = replaced[a], replaced[a-1]

num_to_ind = {v:i for i, v in enumerate(replaced)}

for i in range(M):
    print(num_to_ind[aa[i]] + 1)
