S = input()


def f(r, l):
    r_i = r
    l_i = l
    while r_i < l_i:
        if S[r_i] != S[l_i]:
            return False
        r_i += 1
        l_i -= 1

    return True


len_s = len(S)

ans = 1
for i in range(len_s):
    for j in range(len_s-1, i, -1):
        if f(i, j):
            ans = max(ans, j-i+1)
            break

print(ans)
