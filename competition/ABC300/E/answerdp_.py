MOD = 998244353

N = int(input())

dp = dict()

def f(n):
    if n in dp:
        return dp[n]
    if n == 0 or n == 1:
        return n

    ret = 0
    for i in range(2, 6+1):
        if n % i == 0:
            ret += f(n//i) *  pow(5, MOD - 2, MOD)
            ret %= MOD
    dp[n] = ret
    return ret

print(f(N))