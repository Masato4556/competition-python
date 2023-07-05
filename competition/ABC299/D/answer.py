
N = int(input())

left = 1
right = N
while True:
    mid = (left + right) // 2

    print(f"? {mid}")
    s_i = int(input())
    if s_i == 0:
        left = mid
    else:
        right = mid

    if right - left == 1:
        print(f"! {left}")
        exit()
