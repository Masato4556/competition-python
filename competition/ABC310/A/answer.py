
N, P, Q = map(int, input().split())
D = list(map(int, input().split()))

D_min = min(D)
if P-Q > D_min:
    print(Q+D_min)
else:
    print(P)
