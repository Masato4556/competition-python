from math import ceil
N = int(input())

s = input()

t_cnt = 0
s_cnt = 0
for i in range(N):
    if s[i] == "T":
        t_cnt += 1
    else:
        s_cnt += 1

    if t_cnt == ceil(N/2):
        print("T")
        exit()

    if s_cnt == ceil(N/2):
        print("A")
        exit()
