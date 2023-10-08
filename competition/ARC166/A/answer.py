t = int(input())

for _ in range(t):
    n, x, y = input().split()
    n = int(n)
    x = list(x)
    y = list(y)

    ans = "Yes"

    d = []
    for i in range(n):
        if x[i] == "C" and y[i] == "C":
            x[i] = "X"
            y[i] = "X"

    x = "".join(x).split("X")
    y = "".join(y).split("X")
    x = [list(v) for v in x]
    y = [list(v) for v in y]

    cnt = 0
    not_used_c_x = 0
    for t in range(len(x)):
        if x[t] == "":
            continue

        num = y[t].count("B") - x[t].count("B")
        # tx = []
        for x_i in range(len(x[t])-1, -1, -1):
            if x[t][x_i] == "C":
                if num > 0:
                    x[t][x_i] = "B"
                    num -= 1
                else:
                    x[t][x_i] = "A"
        # print(x[t], y[t])

        for i in range(len(x[t])):
            cnt -= 1 if x[t][i] == "B" else 0
            cnt += 1 if y[t][i] == "B" else 0

            if x[t][i] == "C" and y[t][i] == "C":
                if not_used_c_x < cnt:
                    ans = "No"
                    break
                cnt = 0
                not_used_c_x = 0

            if cnt < 0:
                ans = "No"
                break

            if x[t][i] == "C" and y[t][i] != "C":
                not_used_c_x += 1

            if y[t][i] == "C":

                if x[t][i] != "C":
                    ans = "No"
                    break

        if not_used_c_x < cnt:
            ans = "No"
    print(ans)
