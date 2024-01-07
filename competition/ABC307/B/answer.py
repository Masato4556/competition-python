
N = int(input())
S = [input().strip() for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        t = S[i] + S[j]
        is_palindrome = True
        for k in range(len(t)//2):
            if t[k] != t[-k-1]:
                is_palindrome = False
                break

        if is_palindrome:
            print("Yes")
            exit()

print("No")
