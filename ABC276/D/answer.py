def f(x):
    pow_2 = 0
    while True:
        if x % 2 != 0: break
        x //= 2
        pow_2 += 1

    pow_3 = 0
    while True:
        if x % 3 != 0: break
        x //= 3
        pow_3 += 1

    return (pow_2, pow_3, x)
         



n = int(input())

pow_2_list = []
pow_3_list = []
r_list = []

for a in map(int, input().split()):
    pow_2, pow_3, r = f(a)
    pow_2_list.append(pow_2)
    pow_3_list.append(pow_3)
    r_list.append(r)

if not all([r == r_list[0] for r in r_list]):
    print(-1)
    exit()

min_pow_2 = min(pow_2_list)
min_pow_3 = min(pow_3_list)

print(sum([pow_2 - min_pow_2 for pow_2 in pow_2_list]) + sum([pow_3 - min_pow_3 for pow_3 in pow_3_list]))
