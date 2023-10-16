# テストデータ生成など、回答とは関係のないコードを実行するファイル
from math import log


def calc_divisor(n):
    i = 1
    divisors = []
    while i*i <= n:
        if n % i == 0:
            divisors.append(i)
            q = n // i
            if q != i:
                divisors.append(q)
        i += 1

    divisors.sort()
    return divisors


def solve(A, B):
    divisors = calc_divisor(A**B)
    # print(divisors)

    acc = 1
    for divisor in divisors:
        acc *= divisor
    print(B)
    print(len(divisors), log(acc, A))
    # print()


A = 2*2*5
B = 3

# for a in (2*2*5, 1):
#     print("=======", a)
#     for b in range(0, 10):
#         solve(a, b)

solve(2, 1)
solve(2, 2)
solve(2, 3)
solve(2, 4)
solve(2, 5)
solve(2, 6)
solve(2, 7)
solve(2, 8)
solve(2, 9)
solve(2, 10)
solve(2, 11)
solve(2, 12)

print("====")

solve(2*2, 1)
solve(2*2, 2)
solve(2*2, 3)
solve(2*2, 4)
solve(2*2, 5)
solve(2*2, 6)

print("====")

solve(2**3, 1)
solve(2**3, 2)
solve(2**3, 3)
solve(2**3, 4)
solve(2**3, 5)
solve(2**3, 6)

print("====")

solve(2**4, 1)
solve(2**4, 2)
solve(2**4, 3)
solve(2**4, 4)
solve(2**4, 5)
solve(2**4, 6)

print("====")

solve(2**2 * 3**2, 1)
solve(2**2 * 3**2, 2)
solve(2**2 * 3**2, 3)
solve(2**2 * 3**2, 4)
solve(2**2 * 3**2, 5)
solve(2**2 * 3**2, 6)
