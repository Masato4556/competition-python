def transpose(A):
    return ["".join(a) for a in zip(*A)]


H, W = map(int, input().split())

S = []
T = []
for _ in range(H):
    S.append(input())

for _ in range(H):
    T.append(input())

S_t = transpose(S)
T_t = transpose(T)

counter = dict()

for col in S_t:
    if col not in counter:
        counter[col] = 0
    counter[col] += 1

for col in T_t:
    if col not in counter:
        print("No")
        exit()
    counter[col] -= 1

for k, v in counter.items():
    if v != 0:
        print("No")
        exit()

print("Yes")
