N = int(input())

j_list = [j for j in range(1, 10) if N % j ==0]

ans = []
for i in range(N+1):
    t = "-"
    for j in j_list:
        if i % (N//j) == 0:
            t = str(j)
            break
    ans.append(t)

print("".join(ans))