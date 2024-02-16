from collections import deque

N, M = map(int, input().split())
S = list(input())
T = input()


def canErase(i, S, T):
    N = len(S)
    M = len(T)
    erased_num = 0
    if i+M > N:
        return False

    for j in range(M):
        if S[i+j] == T[j]:
            erased_num += 1
            continue
        if S[i+j] == "#":
            continue
        return False

    return True if erased_num > 0 else False


que = deque([])

for i in range(N-M+1):
    if canErase(i, S, T):
        que.append(i)

while len(que):
    i = que.popleft()
    for j in range(M):
        S[i+j] = "#"

    for k in range(max(0, i-M+1), min(N, i+M)):

        if canErase(k, S, T):
            que.append(k)

print("Yes" if S.count('#') == N else "No")
