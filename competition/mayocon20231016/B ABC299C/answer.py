N = int(input())
S = [len(v) for v in input().split("-")]

if len(S) < 2:
    print(-1)
    exit()

if max(S) == 0:
    print(-1)
    exit()

print(-1 if max(S) == 0 else max(S))
