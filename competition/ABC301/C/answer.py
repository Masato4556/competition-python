from collections import defaultdict

S = input()
T = input()

valid_char = {"a", "t", "c", "o", "d", "e", "r"}

s_dict = defaultdict(int)
t_dict = defaultdict(int)
chars = set()

for s in S:
    s_dict[s] += 1
    if s != "@":
        chars.add(s)

for t in T:
    t_dict[t] += 1
    if t != "@":
        chars.add(t)

for c in chars:
    if c not in valid_char and s_dict[c] != t_dict[c]:
        print("No")
        exit()
    if s_dict[c] < t_dict[c]:
        s_dict["@"] -= t_dict[c] - s_dict[c]
        if s_dict["@"] < 0:
            print("No")
            exit()
    elif s_dict[c] > t_dict[c]:
        t_dict["@"] -= s_dict[c] - t_dict[c]
        if t_dict["@"] < 0:
            print("No")
            exit()

print("Yes")
