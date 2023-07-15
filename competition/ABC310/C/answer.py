
N = int(input())

S = set()
for _ in range(N):
    s = input()
    s_r = s[::-1]
    S.add(min(s, s_r))

print(len(S))
