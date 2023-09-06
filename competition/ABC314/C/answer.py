from collections import defaultdict, deque

N, M = map(int, input().split())
S = input()
C = list(map(int, input().split()))

s_group_by_c = defaultdict(deque)


for i in range(N):
    s_group_by_c[C[i]].append(S[i])

for k in s_group_by_c.keys():
    s_group_by_c[k].rotate(1)

ans = []
for i in range(N):
    ans.append(s_group_by_c[C[i]].popleft())

print("".join(ans))
