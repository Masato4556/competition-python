input()
H = list(map(int, input().split()))
max_h = max(H)
print(H.index(max_h) + 1)