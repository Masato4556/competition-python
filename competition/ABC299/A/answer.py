

_ = input()

S = input()

cnt = 0
for s in S:
    if s == "|":
        cnt += 1
    elif s == "*" and cnt == 1:
        print("in")
        exit()

print("out")