n = int(input())
A = list(map(int, input().split()))

depth_list = [-1 for _ in range(2*n + 1)]
depth_list[0] = 0

for i in range(n):
    depth_list[2*(i+1) - 1] = depth_list[A[i]-1] + 1
    depth_list[2*(i+1)] = depth_list[A[i]-1] + 1

for depth in depth_list:
    if depth == -1:
        continue
    print(depth)
