
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    head_cnt = s.count("1")
    if head_cnt % 2 == 1: 
        print(-1)
    elif head_cnt == 2 and "11" in s: 
        if n <= 3:
            print(-1)
        elif n == 4 and s == "0110": 
            print(3)
        else:
            print(2) 
    else:
        print(head_cnt // 2)

