from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))

INF = 10 ** 18
A.sort()
# print(A)

que = deque(A)

ans = 0
plates = [0] * M

toasts_num = N
plates_num = M
toast_ind = 0

while toasts_num / 2 < plates_num:
    a = que.pop()
    ans += a**2
    toast_ind += 1
    toasts_num -= 1
    plates_num -= 1

# print(ans, toast_ind)

while len(que):
    a_max = que.pop()
    a_min = que.popleft()
    ans += (a_max + a_min)**2
# print(que)
print(ans)
