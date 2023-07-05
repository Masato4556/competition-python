N, M = map(int, input().split())

def f(n):
    ret = 1
    for i in range(n):
        ret *= 10
        ret += 1
    return ret

a = set()
dp = []  
ans_digit = -1
ans_num = -1
for i in range(1, 10):
    x = 0
    for j in range(0, N):
        x = (10 * x + i) % M
        if x == 0:
            if j > ans_digit or (j == ans_digit and i > ans_num):
                ans_digit = j
                ans_num = i
        
if ans_digit != -1:
    print(f(ans_digit) * ans_num)
    exit()
print(-1)