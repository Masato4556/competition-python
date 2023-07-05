
N, K = map(int, input().split())
A = set(map(int, input().split()))

for i in range(K):
    if i not in A:
        print(i)
        exit()

print(K)
