
A, B, W = map(int, input().split())
W *= 1000

total_weight_range = [0, 0]
ans = [-1, -1]
num = 0
while total_weight_range[0] <= W:
    num += 1
    total_weight_range[0] += A
    total_weight_range[1] += B

    if total_weight_range[0] <= W <= total_weight_range[1]:
        if ans[0] == -1:
            ans[0] = num
        ans[1] = num

if ans[0] == -1 and ans[1] == -1:
    print("UNSATISFIABLE")
else:
    print(*ans)