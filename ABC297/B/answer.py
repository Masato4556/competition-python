
S = input()

first_b_i = -1
first_r_1 = -1
k_i = -1
for i in range(len(S)):
    if S[i] == "B":
        if first_b_i == -1:
            first_b_i = i
        else:
            if i % 2 == first_b_i % 2:
                print("No")
                exit()
    elif S[i] == "R":
        if first_r_1 == -1:
            first_r_1 = i
        else:
            if not (first_r_1 < k_i < i) :
                print("No")
                exit()
    elif S[i] == "K":
        k_i = i

print("Yes")