INF = 10**19
N, M = map(int, input().split())

if N >= M:
    print(M)
    exit()

ans = INF
for a in range(1, N+1):
    b = (M+a-1) // a
    if b <= N: ans=min(ans, a*b)
    if a>b: break
    
print(ans if ans != INF else -1)