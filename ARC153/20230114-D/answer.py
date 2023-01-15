def f(num):
    s = str(num)
    return sum([int(s_v) for s_v in s])

n = int(input())
A = list(map(int, input().split()))


X = [0] * 9

result = 10**9
x_result = []
for ex in range(9):
    if ex != 0:
         X[ex] = X[ex-1]

    for i in range(10):
        i2 = (i * (10**ex)) + X[ex-1]
        total = 0
        for a_v in A:
            total += f(a_v + i2)
        if total < result:
            result = total
            X[ex] = i2

print(result)



