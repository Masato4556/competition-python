
N = int(input())

x_cnt = 0
y_cnt = 0
for _ in range(N):
    x, y = map(int, input().split())
    x_cnt += x
    y_cnt += y

if x_cnt > y_cnt:
    print("Takahashi")
elif x_cnt < y_cnt:
    print("Aoki")
else:
    print("Draw")
