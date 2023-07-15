from math import floor, log
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    
    while N>0:
        K -= N % 3
        N //= 3
    print("Yes" if K >= 0 and K % 2 == 0 else 'No')
