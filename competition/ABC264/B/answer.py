r, c = map(int, input().split())

x, y = (c, r) if abs(r-8) > abs(c-8) else (r, c)
if y % 2 == 0: 
    if min(y, 16-y) <= x <= max(y, 16-y):
        print("white")
    elif x % 2 == 0:
        print("white")
    else:
        print("black")
else:
    if min(y, 16-y) <= x <= max(y, 16-y):
        print("black")
    elif x % 2 == 0:
        print("white")
    else:
        print("black")
