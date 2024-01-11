N, Q = map(int, input().split())
G = set()
for _ in range(Q):
    t, a, b = map(int, input().split())
    a -= 1
    b -= 1

    if t == 1:
        G.add((a, b))
    elif t == 2:
        if (a, b) in G:
            G.remove((a, b))
    else:
        print("Yes" if (a, b) in G and (b, a) in G else "No")
