t = int(input())

for _ in range(t):
    n, x, y = input().split()
    n = int(n)

    ans = "Yes"

    b_cnt_x = 0
    b_cnt_y = 0
    not_used_c_x = 0
    for i in range(n):
        b_cnt_x += 1 if x[i] == "B" else 0
        b_cnt_y += 1 if y[i] == "B" else 0

        if b_cnt_x > b_cnt_y:
            ans = "No"
            break

        if x[i] == "C" and y[i] != "C":
            not_used_c_x += 1

        if y[i] == "C":

            if x[i] != "C":
                ans = "No"
                break
            if b_cnt_x + not_used_c_x < b_cnt_y:
                ans = "No"
                break
            b_cnt_x = 0
            b_cnt_y = 0
            not_used_c_x = 0
        # print(i, x[i], y[i])

    if b_cnt_x + not_used_c_x < b_cnt_y:
        ans = "No"
    print(ans)
