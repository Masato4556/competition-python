N = int(input())

ans = ['-'] * (N+1)
for i in range(N+1):
    for j in range(1, 10):
        if N % j != 0:
            continue
        if i % (N // j) == 0:
            ans[i] = str(j)
            break
print(''.join(ans))
