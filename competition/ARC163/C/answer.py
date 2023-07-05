t = int(input())

for _ in range(t):
    n = int(input())

    if n == 1:
        print("Yes")
        print(1)
        continue
    elif n == 2:
        print("No")
        continue

    A = set()
    for i in range(1, n):
        A.add(i * (i+1))

    cnt = 0
    while True:
        i = n - cnt
        if 2**cnt*(n-cnt) not in A:
            A.add(2**cnt*(n-cnt))
            print("Yes")
            print(*A)
            break
        A = {2 * a for a in A if a != 2**cnt * (i-1) * i}
        A.add(2)
        cnt += 1
