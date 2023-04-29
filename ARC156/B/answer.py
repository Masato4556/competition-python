from collections import deque
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 回答に影響しない配列Aの要素を削除
A_set = set(A)
cnt = 0
for i in range(N+K):
    if i not in A_set:
        cnt += 1
    if cnt == K:
        break
max_a = i
A = [a for a in A if a <= max_a]
A_set = set(A)

for i in range(max_a+1):
    if i in A_set: break
    A_set.add(i)
    K -= 1

print(A_set)
print(K)
