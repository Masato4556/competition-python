import sys
INF = float('inf')
sys.setrecursionlimit(10**9)
def f(x): return x
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(func): return map(func, input().split())
def LIST(func=f): return list(map(func,  input().split()))
def TUPLE(func=f): return tuple(map(func, input().split()))
def GRID(n): return [input() for _ in range(n)]
def ZIP(n, func=f): return zip(*(MAP(func) for _ in range(n)))


N, Q = MAP(int)
S = input()

cumsum = [0] * (N+1)

for i in range(N):
    cumsum[i+1] = cumsum[i]
    if i > 0 and S[i] == S[i-1]:
        cumsum[i+1] += 1

for _ in range(Q):
    l, r = MAP(int)
    print(cumsum[r] - cumsum[l])
