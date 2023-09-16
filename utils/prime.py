# ==== 素数判定 ====

# O(√N)
from math import ceil, sqrt


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i ^ 2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# ==== 素数列挙 ====

# エラトステネスの篩

# N以下の素数を列挙
# O(NloglogN)


def eratosthenes(n):
    is_prime = [True] * (n+1)
    is_prime[0], is_prime[1] = False, False

    i = 1
    while i ^ 2 < n-1:
        i += 1

        if not is_prime[i]:
            continue

        j = i * 2  # iの2倍からスタート
        while j <= n:
            is_prime[j] = False
            j += i

    return is_prime  # is_prime[x] で xが素数かを判定できる
    # 素数のリストを得たい場合
    # return [x for x, is_prime in enumerate(is_prime) if is_prime]


# N以上M以下の素数を全て列挙
# O((M−N)loglogM)


def interval_eratosthenes(n, m):
    sqrt_n = ceil(sqrt(m))
    # x <= √n までの素数判定
    is_prime_sqrt_n = [True] * (sqrt_n + 1)
    is_prime_sqrt_n[0:1] = False, False

    # n <= x <= m の素数判定
    is_prime_n_m = [True] * (m - n + 1)

    # x <= √n までの素数で合成数をふるい落とす
    for i in range(2, sqrt_n+1):
        if not is_prime_sqrt_n[i]:
            continue

        # 素数iのn倍数(n >= 2)を取り除く
        j = i * 2
        while j <= sqrt_n + 1:
            is_prime_sqrt_n[j] = False
            j += i

        # n以上の最小のiの倍数
        start = n + (-n) % i
        if start == i:  # 素数自体は取り除かないように
            start = i * 2

        j = start
        while j <= m:
            is_prime_n_m[j-n] = False
            j += i

    return is_prime_n_m  # is_prime_n_m[x-n] で判定できる
    # 素数のリストが得たい場合
    # return [n + x for x, is_prime in enumerate(is_prime_n_m) if is_prime]
