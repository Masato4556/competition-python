N = int(input())
G = {i+1:p for i, p in enumerate(map(lambda x: int(x)-1, input().split()))}

cnt = 0
curr = N-1
while True:
    cnt += 1
    curr = G[curr] 
    if curr == 0:
        break
print(cnt)